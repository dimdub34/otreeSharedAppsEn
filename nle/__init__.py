import os
import random
import statistics
from pathlib import Path

from otree.api import *

app_name = Path(__file__).parent.name

doc = """
NEL - Number Line Estimation <br>
Siegler, R. S., & Opfer, J. E. (2003). The development of numerical estimation: Evidence for multiple 
representations of numerical quantity. Psychological Science, 14(3), 237-243.
"""


class C(BaseConstants):
    NAME_IN_URL = 'nle'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    NB_TARGETS = 10
    NLE_TIME = 10
    CONSTANTE = 5  # gain si cible exacte
    FACTEUR_DISTANCE = 0.05  # payoff = CONSTANTE - 0.05 x distance where distance = |target - cursor position|
    NLE_VALUES = [18.09, 85.03, 8.11, 77.09, 92.17, 14.64, 59.99, 93.17, 9.11, 17.76]


class Subsession(BaseSubsession):
    nle_values = models.StringField()


def creating_session(subsession: Subsession):
    subsession.nle_values = "-".join(list(map(str, C.NLE_VALUES)))


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    nle_paid_game = models.IntegerField()

    # -- STANDARD
    nle_1 = models.FloatField()
    nle_2 = models.FloatField()
    nle_3 = models.FloatField()
    nle_4 = models.FloatField()
    nle_5 = models.FloatField()
    nle_6 = models.FloatField()
    nle_7 = models.FloatField()
    nle_8 = models.FloatField()
    nle_9 = models.FloatField()
    nle_10 = models.FloatField()
    nle_avg_distance = models.FloatField()
    nle_payoff = models.CurrencyField()

    def compute_nle_payoff(self):
        targets = C.NLE_VALUES
        differences = [abs(getattr(self, f"nle_{i}") - targets[i - 1]) for i in range(1, C.NB_TARGETS + 1)]
        self.nle_avg_distance = round(statistics.mean(differences), 2)
        self.nle_payoff = cu(C.CONSTANTE - C.FACTEUR_DISTANCE * self.nle_avg_distance)
        txt_final = (f"Your average distance between the target value and your cursor position "
                     f"was {self.nle_avg_distance}. Your payoff is therefore "
                     f"{self.nle_payoff}.")
        self.participant.vars[app_name] = dict(txt_final=txt_final, payoff=self.nle_payoff)


# ======================================================================================================================
#
# -- PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def vars_for_template(player: Player):
        return dict()

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False),
            **C.__dict__.copy()
        )


class Instructions(MyPage):
    pass


class Decision(MyPage):
    form_model = "player"
    form_fields = [f"nle_{i}" for i in range(1, C.NB_TARGETS + 1)]

    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        existing["nle_values"] = player.subsession.nle_values.split("-")
        return existing

    @staticmethod
    def js_vars(player: Player):
        existing = MyPage.js_vars(player)
        existing["nle_values"] = player.subsession.nle_values.split("-")
        return existing

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for i in range(1, C.NB_TARGETS + 1):
                setattr(player, f"nle_{i}", round(random.uniform(0, 100), 2))
            player.participant._is_bot = True
        player.compute_nle_payoff()


class Results(MyPage):
    @staticmethod
    def vars_for_template(player: Player):
        existing = MyPage.vars_for_template(player)
        targets = list(map(float, player.subsession.nle_values.split("-")))
        positions = [getattr(player, f"nle_{i}") for i in range(1, C.NB_TARGETS + 1)]
        distances = [round(abs(targets[i] - positions[i]), 2) for i in range(10)]
        targets_numbers = list(zip(targets, positions, distances))
        existing["targets_numbers"] = targets_numbers
        return existing


page_sequence = [
    Instructions, Decision, Results
]
