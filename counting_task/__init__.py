from otree.api import *
import random

doc = """
Counting task: count digits in grids composed of digits 0 to 9
"""


class C(BaseConstants):
    NAME_IN_URL = 'counting_task'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    TIME_LIMIT = 120  # seconds
    REQUIRED_SUCCESS = 2
    PAYOFF_SUCCESS = 100
    GRID_SIZE = 10


class Subsession(BaseSubsession):
    pass


def vars_for_admin_report(subsession: Subsession):
    players_infos = list()
    for p in subsession.get_players():
        players_infos.append({
            "code": p.participant.code,
            "label": p.participant.label,
            "nb_success": p.num_successful_counting
        })
    return dict(players_infos=players_infos)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    num_successful_counting = models.IntegerField(initial=0)
    payoff_ecu = models.IntegerField(initial=0)

    def compute_payoff(self):
        if self.num_successful_counting >= C.REQUIRED_SUCCESS:
            self.payoff_ecu = C.PAYOFF_SUCCESS
        self.payoff = cu(self.payoff_ecu)
        txt_final = (f"You had to validate {C.REQUIRED_SUCCESS} grids, and you validated "
                     f"{self.num_successful_counting}. <br/>")
        if self.num_successful_counting >= C.REQUIRED_SUCCESS:
            txt_final += f"You can continue the experiment with an endowment of {self.payoff_ecu} ECU."
        else:
            txt_final += "You cannot continue the experiment."
        self.participant.vars["counting_task"] = dict(
            txt_final=txt_final,
            payoff_ecu=self.payoff_ecu,
            payoff=self.payoff,
        )


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
def format_time(seconds):
    minutes = seconds // 60
    seconds = seconds % 60
    txt = f"{minutes} minutes"
    if seconds > 0:
        txt += f" and {seconds} seconds"
    return txt


def common_vars(player: Player):
    return dict(
        time_limit=format_time(C.TIME_LIMIT),
    )


class Instructions(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {**common_vars(player)}


class Counting(Page):
    form_model = 'player'
    form_fields = ["num_successful_counting"]
    timeout_seconds = C.TIME_LIMIT

    @staticmethod
    def vars_for_template(player: Player):
        return {**common_vars(player)}

    @staticmethod
    def js_vars(player: Player):
        local_vars = dict(
            grid_size=C.GRID_SIZE,
        )
        return {**common_vars(player), **local_vars}

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        """
        No need to use timeout_happened here because the page already has a timer.
        """
        player.compute_payoff()


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return {**common_vars(player)}


page_sequence = [
    Instructions,
    Counting, Results
]
