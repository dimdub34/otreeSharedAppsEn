import random

from otree.api import *

doc="R. Christie‚ F. Geis. Studies in Machiavellianism. NY: Academic Press, 1970"
class C(BaseConstants):
    NAME_IN_URL = 'mach_iv'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1

    # questions MACH-IV
    QUESTIONS_MACH = [
        {"id": 1, "text": "Never tell anyone the real reason you did something unless it is useful to do so."},
        {"id": 2, "text": "The best way to handle people is to tell them what they want to hear."},
        {"id": 3, "text": "One should take action only when sure it is morally right."},
        {"id": 4, "text": "Most people are basically good and kind."},
        {"id": 5,
         "text": "It is safest to assume that all people have a vicious streak, and it will come out when they are given a chance."},
        {"id": 6, "text": "Honesty is the best policy in all cases."},
        {"id": 7, "text": "There is no excuse for lying to someone else."},
        {"id": 8, "text": "Generally speaking, people won't work hard unless they're forced to do so."},
        {"id": 9, "text": "All in all, it is better to be humble and honest than to be important and dishonest."},
        {"id": 10,
         "text": "When you ask someone to do something for you, it is best to give the real reasons for wanting it rather than giving reasons which carry more weight."},
        {"id": 11, "text": "Most people who get ahead in the world lead clean, moral lives."},
        {"id": 12, "text": "Anyone who completely trusts anyone else is asking for trouble."},
        {"id": 13,
         "text": "The biggest difference between most criminals and other people is that the criminals are stupid enough to get caught."},
        {"id": 14, "text": "Most people are brave."},
        {"id": 15, "text": "It is wise to flatter important people."},
        {"id": 16, "text": "It is possible to be good in all respects."},
        {"id": 17, "text": "P. T. Barnum was wrong when he said 'there's a sucker born every minute.'"},
        {"id": 18, "text": "It is hard to get ahead without cutting corners here and there."},
        {"id": 19,
         "text": "People suffering from incurable diseases should have the choice of being put painlessly to death."},
        {"id": 20, "text": "Most people forget more easily the death of their parents than the loss of their property."},
    ]
    NUM_QUESTIONS = len(QUESTIONS_MACH)
    QUESTIONS_MACH_DICT = {q['id']: q for q in QUESTIONS_MACH}

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    mach_score = models.IntegerField()

    def set_mach_score(self):
        self.mach_score = sum(
            getattr(self, f'mach_{q["id"]}')
            for q in C.QUESTIONS_MACH
        )


# Fields generation
for q in C.QUESTIONS_MACH:
    setattr(Player, f'mach_{q["id"]}', models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        widget=widgets.RadioSelectHorizontal,
        label=q["text"]
    ))


class MachPage(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [f'mach_{i}' for i in range(1, C.NUM_QUESTIONS + 1)]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            for i in range(1, C.NUM_QUESTIONS + 1):
                setattr(player, f'mach_{i}', random.randint(1, 5))
        player.set_mach_score()


page_sequence = [MachPage]
