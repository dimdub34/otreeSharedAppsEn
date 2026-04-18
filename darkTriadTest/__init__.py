import random

from otree.api import *

doc = "SD3 (Short Dark Triad) - Paulhus, 2013"


class C(BaseConstants):
    NAME_IN_URL = 'shortDarkTriad'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # SD3 - 27 items (9 Mach, 9 Narc, 9 Psych)
    QUESTIONS_SD3 = [
        # MACHIAVELLIANISM
        {"id": 1, "text": "It's not wise to tell your secrets.", "rev": False},
        {"id": 2, "text": "I like to use clever manipulation to get my way.", "rev": False},
        {"id": 3, "text": "Whatever it takes, you must get the important people on your side.", "rev": False},
        {"id": 4, "text": "Avoid direct conflict with others because they may be useful in the future.", "rev": False},
        {"id": 5, "text": "It’s wise to keep track of information that you can use against people later.",
         "rev": False},
        {"id": 6, "text": "You should wait for the right time to get back at people.", "rev": False},
        {"id": 7, "text": "There are things you should hide from other people to preserve your reputation.",
         "rev": False},
        {"id": 8, "text": "Make sure your plans benefit yourself, not others.", "rev": False},
        {"id": 9, "text": "Most people can be manipulated.", "rev": False},

        # NARCISSISM
        {"id": 10, "text": "People see me as a natural leader.", "rev": False},
        {"id": 11, "text": "I hate being the center of attention.", "rev": True},  # Reversed
        {"id": 12, "text": "Many group activities tend to be dull without me.", "rev": False},
        {"id": 13, "text": "I know that I am special because everyone keeps telling me so.", "rev": False},
        {"id": 14, "text": "I like to get acquainted with important people.", "rev": False},
        {"id": 15, "text": "I feel embarrassed if someone compliments me.", "rev": True},  # Reversed
        {"id": 16, "text": "I have been compared to famous people.", "rev": False},
        {"id": 17, "text": "I am an average person.", "rev": True},  # Reversed
        {"id": 18, "text": "I insist on getting the respect I deserve.", "rev": False},

        # PSYCHOPATHY
        {"id": 19, "text": "I like to get revenge on authorities.", "rev": False},
        {"id": 20, "text": "I avoid dangerous situations.", "rev": True},  # Reversed
        {"id": 21, "text": "Payback needs to be quick and nasty.", "rev": False},
        {"id": 22, "text": "People often say I’m out of control.", "rev": False},
        {"id": 23, "text": "It’s true that I can be mean to others.", "rev": False},
        {"id": 24, "text": "People who mess with me always regret it.", "rev": False},
        {"id": 25, "text": "I have never gotten into trouble with the law.", "rev": True},  # Reversed
        {"id": 26, "text": "I enjoy having sex with people I hardly know.", "rev": False},
        {"id": 27, "text": "I’ll say anything to get what I want.", "rev": False},
    ]
    NUM_QUESTIONS = len(QUESTIONS_SD3)
    QUESTIONS_DICT = {q['id']: q for q in QUESTIONS_SD3}


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score_mach = models.FloatField()
    score_narc = models.FloatField()
    score_psych = models.FloatField()

    def set_sd3_scores(self):
        def get_val(idx):
            q = C.QUESTIONS_DICT[idx]
            val = getattr(self, f'sd3_{idx}')
            return (6 - val) if q['rev'] else val

        self.score_mach = sum(get_val(i) for i in range(1, 10)) / 9
        self.score_narc = sum(get_val(i) for i in range(10, 19)) / 9
        self.score_psych = sum(get_val(i) for i in range(19, 28)) / 9


for q in C.QUESTIONS_SD3:
    setattr(Player, f'sd3_{q["id"]}', models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        widget=widgets.RadioSelectHorizontal,
        label=q['text'],
    ))


class DarkTriadPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [f'sd3_{i}' for i in range(1, C.NUM_QUESTIONS + 1)]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for i in range(1, C.NUM_QUESTIONS + 1):
                setattr(player, f'sd3_{i}', random.randint(1, 5))
        player.set_sd3_scores()


page_sequence = [DarkTriadPage]
