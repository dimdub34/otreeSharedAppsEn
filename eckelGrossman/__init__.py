import random

from otree.api import *
from pathlib import Path

app_name = Path(__file__).parent.name

doc = """
Measurement of risk attitude using the Binswanger method (1980), as used by Eckel & Grossman (2002, 2008). <br>
The lottery values are from the paper: <br>
Dave, C., Eckel, C.C., Johnson, C.A. et al. Eliciting risk preferences: When is simple better?. J Risk Uncertain 41, 
219–243 (2010). https://doi.org/10.1007/s11166-010-9103-z <br>
The values are divided by 10 to represent Euros (control task).
"""


class C(BaseConstants):
    NAME_IN_URL = 'biswanger'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    LOTERIES = {
        1: (2.8, 2.8), 2: (2.4, 3.6), 3: (2.0, 4.4), 4: (1.6, 5.2), 5: (1.2, 6.0), 6: (0.2, 7.0)
    }
    NUM_LOTERIES = len(LOTERIES)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    lottery_choice = models.IntegerField(choices=list(C.LOTERIES.keys()))
    lottery_randomVal = models.IntegerField(
        doc="If random value <= 50 the payoff is equal to the left value in the chosen lottery, otherwise it is "
            "equal to the right one.")

    def compute_payoff(self):
        self.lottery_randomVal = random.randint(1, 100)
        self.payoff = cu(C.LOTERIES[self.lottery_choice][self.lottery_randomVal > 50])
        txt_final = (f"You chose lottery {self.lottery_choice}: 50% chance of winning "
                     f"{cu(C.LOTERIES[self.lottery_choice][0])} and 50% chance of winning "
                     f"{cu(C.LOTERIES[self.lottery_choice][1])}. <br>"
                     f"After the random draw, your payoff is {self.payoff}.")
        self.participant.vars[app_name] = dict(txt_final=txt_final, payoff=self.payoff)


# ======================================================================================================================
#
# PAGES
#
# ======================================================================================================================
class MyPage(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))


class Decision(MyPage):
    form_model = "player"
    form_fields = ["lottery_choice"]

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False)
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.participant._is_bot = True
            player.lottery_choice = random.choice(list(C.LOTERIES.keys()))
        player.compute_payoff()

class Result(MyPage):
    pass


page_sequence = [Decision, Result]
