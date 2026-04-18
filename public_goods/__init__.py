import random

import numpy as np
from otree.api import *
from _commons.useful_functions import get_minutes

author = 'D. Dubois'

doc = """
Public goods game
"""


class C(BaseConstants):
    NAME_IN_URL = 'public_goods'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10

    ENDOWMENT = 20
    CHAT_TIME = 120  # seconds


class Subsession(BaseSubsession):
    fill_auto = models.BooleanField()
    mpcr = models.FloatField()
    seuil = models.IntegerField()
    display_contributions_individuelles = models.BooleanField()
    players_per_group = models.IntegerField()
    chat = models.BooleanField()


def creating_session(subsession: Subsession):
    subsession.fill_auto = subsession.session.config.get("fill_auto", False)
    subsession.mpcr = subsession.session.config.get("mpcr", 0.5)
    subsession.seuil = subsession.session.config.get("seuil", 0)
    subsession.display_contributions_individuelles = subsession.session.config.get(
        "display_contributions_individuelles", False)
    subsession.players_per_group = subsession.session.config.get("players_per_group", 4)
    subsession.chat = subsession.session.config.get("chat", False)

    # group formation
    if subsession.round_number == 1:
        players = subsession.get_players()
        random.shuffle(players)
        subsession.set_group_matrix(np.array_split(players, len(players) / subsession.players_per_group))
    else:
        subsession.group_like_round(1)


def _get_player_contributions(player):
    """Retrieve a player's contributions across all rounds."""
    return [r.field_maybe_none("public_account") or 0 for r in player.in_all_rounds()]


def vars_for_admin_report(subsession: Subsession):
    infos_participants = []
    groups_data = []
    max_endowment = subsession.players_per_group * C.ENDOWMENT

    for g in subsession.get_groups():
        # Participant data
        for p in g.get_players():
            contributions = _get_player_contributions(p)
            infos_participants.append({
                'player': p.id_in_subsession,
                'label': p.participant.label,
                'group': p.group.id_in_subsession,
                'public': contributions,
                'public_mean': np.mean(contributions) if contributions else 0,
                'cumul': p.field_maybe_none("payoff_ecu_cumul")
            })

        # Group chart data
        players = g.get_players()
        group_dict = {
            'total_group': [[r.round_number, r.field_maybe_none("total_public_account")] for r in g.in_all_rounds()],
            'individual_contrib': [[
                [r.round_number, r.field_maybe_none("public_account")] for r in p.in_all_rounds()
            ] for p in players]
        }
        groups_data.append(group_dict)

    infos_graph = {
        'nb_groups': len(subsession.get_groups()),
        'groups_data': groups_data,
        'max_endowment': max_endowment,
        'num_rounds': C.NUM_ROUNDS
    }
    return dict(infos_participants=infos_participants, infos_graph=infos_graph)


class Group(BaseGroup):
    total_public_account = models.IntegerField()

    def compute_total_public_account(self):
        self.total_public_account = sum([p.public_account for p in self.get_players()])
        for p in self.get_players():
            if self.total_public_account >= self.subsession.seuil:
                p.payoff_ecu = p.private_account + self.total_public_account * self.subsession.mpcr
            else:
                p.payoff_ecu = p.private_account
            p.payoff_ecu_cumul = sum([r.payoff_ecu for r in p.in_all_rounds()])


class Player(BasePlayer):
    private_account = models.IntegerField()
    public_account = models.IntegerField(
        label="Enter the number of tokens you place in the public account",
        min=0, max=C.ENDOWMENT
    )
    payoff_ecu = models.FloatField(initial=0)
    payoff_ecu_cumul = models.FloatField()

    def set_final_payoff(self):
        self.participant.payoff = cu(self.payoff_ecu_cumul * self.session.config["real_world_currency_per_point"])

        txt_final = (f"Your cumulative payoff over the {C.NUM_ROUNDS} periods is {self.payoff_ecu_cumul:.2f} ECU, "
                     f"which corresponds to {self.participant.payoff}. <br> Including the participation fee, "
                     f"your <b>total payoff is {self.participant.payoff_plus_participation_fee()}</b>.")
        self.participant.vars["public_goods"] = dict(
            txt_final=txt_final,
            payoff=self.participant.payoff
        )

    def get_historique(self, current_round=False):
        the_rounds = self.in_previous_rounds() if not current_round else self.in_all_rounds()
        historique = [
            {
                "round_number": p.round_number,
                "private_account": p.private_account,
                "public_account": p.public_account,
                "total_public_account": p.group.total_public_account if p.group else None,
                "payoff": p.payoff_ecu,
                "cumulative_payoff": p.payoff_ecu_cumul,
            } for p in the_rounds
        ]
        historique.reverse()
        return historique

# ======================================================================================================================
#
# Pages
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        instructions_exemple_compte_collectif = (
            f"If you place 2 tokens in the public account and the other members of your group place "
            f"3, 0, and 7 tokens respectively, then each group member's payoff from the public account is: "
            f"{player.subsession.mpcr} x (2 + 3 + 0 + 7), "
            f"which is {12 * player.subsession.mpcr:.2f} ECU.")

        instructions_exemple_gain = (
            f"If you place 7 tokens in your private account and 13 tokens in the public account, and the other "
            f"members of your group place 3, 8, and 5 tokens respectively in the public account, then your payoff "
            f"for the period is 7 + 29 x {player.subsession.mpcr} = {7 + 29 * player.subsession.mpcr:.2f} ECU."
        )
        return dict(
            instructions_template="public_goods/InstructionsTemplate.html",
            final_template="public_goods/FinalTemplate.html",
            instructions_exemple_compte_collectif=instructions_exemple_compte_collectif,
            instructions_exemple_gain=instructions_exemple_gain,
            chat_time=get_minutes(C.CHAT_TIME)
        )

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.subsession.fill_auto
        )


class Instructions(MyPage):
    template_name = "global/instructions.html"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1


class InstructionsWaitMonitor(MyPage):
    template_name = "global/instructions_wait_monitor.html"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1

class Chat(MyPage):
    timeout_seconds = C.CHAT_TIME
    timer_text = "Time left:"

    @staticmethod
    def is_displayed(player: Player):
        return player.subsession.chat

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing["historique"] = player.get_historique()
        return existing


class Decision(MyPage):
    form_model = "player"
    form_fields = ["public_account"]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing["historique"] = player.get_historique()
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.public_account = random.randint(0, C.ENDOWMENT)
        player.private_account = C.ENDOWMENT - player.public_account


class DecisionWaitForGroup(WaitPage):
    wait_for_all_groups = False

    @staticmethod
    def after_all_players_arrive(group):
        group.compute_total_public_account()


class Results(MyPage):
    @staticmethod
    def vars_for_template(player: Player):
        others = [p.public_account for p in player.get_others_in_group()]
        if len(others) == 1:
            contrib_others = others[0]
            contrib_others_txt = (
                f"For your information, the other member of your group placed "
                f"{contrib_others} tokens in the public account."
            )
        else:
            contrib_others = f"{', '.join(map(str, others[:-1]))} and {others[-1]}"
            contrib_others_txt = (
                f"For your information, the other members of your group placed "
                f"{contrib_others} tokens in the public account."
            )
        existing = MyPage.vars_for_template(player=player)
        existing["contributions_others_txt"] = contrib_others_txt
        existing["contributions_others"] = contrib_others
        existing["historique"] = player.get_historique(current_round=True)
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.round_number == C.NUM_ROUNDS:
            player.set_final_payoff()


class ResultsWaitForGroup(WaitPage):
    wait_for_all_groups = True


class Final(MyPage):
    template_name = "global/final.html"

    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == C.NUM_ROUNDS


page_sequence = [
    Instructions, InstructionsWaitMonitor,
    Chat,
    Decision, DecisionWaitForGroup,
    Results, ResultsWaitForGroup,
    Final
]
