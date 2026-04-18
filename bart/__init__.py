import random
from pathlib import Path

from otree.api import *

from bret import MyPage

app_name = Path(__file__).parent.name

doc = """
Balloon Risk Analogue Task (BART) <br>
Lejuez, C. W., Read, J. P., Kahler, C. W., Richards, J. B., Ramsey, S. E., Stuart, G. L., Strong, D. R., & Brown, R. A. (2002). 
Evaluation of a behavioral measure of risk taking: The Balloon Analogue Risk Task (BART). 
Journal of Experimental Psychology: Applied, 8(2), 75-84. doi: 10.1037/1076-898X.8.2.75.
"""


class C(BaseConstants):
    NAME_IN_URL = 'bart'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    MAX_PUMPS = 64
    PAYOFF_PER_PUMP = 0.5


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    bart_decision = models.IntegerField(min=1, max=64)
    bart_explosion_value = models.IntegerField()
    bart_explosion = models.BooleanField()

    def compute_payoff(self):
        txt_final = f"You chose to pump the balloon {self.bart_decision} times."
        if self.bart_explosion:
            self.payoff = cu(0)
            txt_final += " The balloon exploded."
        else:
            self.payoff = cu(self.bart_decision * C.PAYOFF_PER_PUMP)
            txt_final += " The balloon did not explode."
        txt_final += "<br>" + f"Your payoff is therefore {self.payoff}."

        self.participant.vars[app_name] = dict(txt_final=txt_final, payoff=self.payoff)


class Decision(Page):
    form_model = "player"
    form_fields = ["bart_decision", "bart_explosion_value", "bart_explosion"]

    @staticmethod
    def js_vars(player: Player):
        return dict(
            fill_auto=player.session.config.get("fill_auto", False),
            payoff_per_pump=C.PAYOFF_PER_PUMP,
            max_pumps=C.MAX_PUMPS
        )

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.bart_decision = random.randint(1, C.MAX_PUMPS)
        player.compute_payoff()



page_sequence = [Decision]
