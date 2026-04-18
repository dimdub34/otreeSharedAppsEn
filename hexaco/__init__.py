import random

from otree.api import *

doc = ("Ashton, M. C., & Lee, K. (2009). The HEXACO–60: A Short Measure of the Major Dimensions of Personality. "
       "Journal of Personality Assessment, 91(4), 340–345. https://doi.org/10.1080/00223890902935878")


class C(BaseConstants):
    NAME_IN_URL = 'hexaco_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    QUESTIONS_HEXACO = [
        {"id": 1, "text": "I would be quite bored by a visit to an art gallery.", "rev": True},
        {"id": 2, "text": "I plan ahead and organize things, to avoid scambling at the last-minute.", "rev": False},
        {"id": 3, "text": "I rarely hold a grudge, even against people who have badly wronged me.", "rev": False},
        {"id": 4, "text": "I feel reasonably satisfied with myself overall.", "rev": False},
        {"id": 5, "text": "I would feel afraid if I had to travel in bad weather conditions.", "rev": False},
        {"id": 6,
         "text": "I wouldn't use flattery to get a raise or promotion at work, even if I thought it would succeed.",
         "rev": False},
        {"id": 7, "text": "I'm interested in learning about the history and politics of other countries.",
         "rev": False},
        {"id": 8, "text": "I often push myself very hard when trying to achieve a goal.", "rev": False},
        {"id": 9, "text": "People sometimes tell me that I am too critical of others.", "rev": True},
        {"id": 10, "text": "I rarely express my opinions in group meetings.", "rev": True},
        {"id": 11, "text": "I sometimes can't help worrying about little things.", "rev": False},
        {"id": 12, "text": "If I knew that I could never be caught, I would be willing to steal a million dollars.",
         "rev": True},
        {"id": 13, "text": "I would enjoy creating a work of art, such as a novel, a song, or a painting.",
         "rev": False},
        {"id": 14, "text": "When working on something, I don't pay much attention to small details.", "rev": True},
        {"id": 15, "text": "People sometimes tell me that I'm too stubborn.", "rev": True},
        {"id": 16, "text": "I prefer jobs that involve active social interaction to those that involve working alone.",
         "rev": False},
        {"id": 17, "text": "When I suffer from a painful experience, I need someone to make me feel comfortable.",
         "rev": False},
        {"id": 18, "text": "Having a lot of money is not especially important to me.", "rev": False},
        {"id": 19, "text": "I think that paying attention to radical ideas is a waste of time.", "rev": True},
        {"id": 20, "text": "I make decisions based on the feelings of the moment rather than on careful thought.",
         "rev": True},
        {"id": 21, "text": "People think of me as someone who has a quick temper.", "rev": True},
        {"id": 22, "text": "On most days, I feel cheerful and optimistic.", "rev": False},
        {"id": 23, "text": "I feel like crying when I see other people crying.", "rev": False},
        {"id": 24, "text": "I think that I am entitled to more respect than the average person is.", "rev": True},
        {"id": 25, "text": "If I had the opportunity, I would like to attend a classical music concert.", "rev": False},
        {"id": 26, "text": "When working, I sometimes have difficulties due to being disorganized.", "rev": True},
        {"id": 27, "text": "My attitude toward people who have treated me badly is 'forgive and forget'.",
         "rev": False},
        {"id": 28, "text": "I feel that I am an unpopular person.", "rev": True},
        {"id": 29, "text": "When it comes to physical danger, I am very fearful.", "rev": False},
        {"id": 30, "text": "If I want something from a someone, I will laugh at that person's worst jokes.",
         "rev": True},
        {"id": 31, "text": "I've never really enjoyed looking through an encyclopedia.", "rev": True},
        {"id": 32, "text": "I do only the minimum amount of work needed to get by.", "rev": True},
        {"id": 33, "text": "I tend to be lenient in judging other people.", "rev": False},
        {"id": 34, "text": "In social situations, I'm usually the one who makes the first move.", "rev": False},
        {"id": 35, "text": "I worry less than most people do.", "rev": True},
        {"id": 36, "text": "I would never accept a bribe, even if it were very large.", "rev": False},
        {"id": 37, "text": "People have often told me that I have a good imagination.", "rev": False},
        {"id": 38, "text": "I always try to be accurate in my work, even at the expense of time.", "rev": False},
        {"id": 39, "text": "I am usually quite flexible in my opinions when people disagree with me.", "rev": False},
        {"id": 40, "text": "The first thing I always do in a new place is to make friends.", "rev": False},
        {"id": 41, "text": "I can handle difficult situations without needing emotional support from anyone else.",
         "rev": True},
        {"id": 42, "text": "I would get a lot of pleasure from owning expensive luxury goods.", "rev": True},
        {"id": 43, "text": "I like people who have unconventional views.", "rev": False},
        {"id": 44, "text": "I make a lot of mistakes because I don't think before I act.", "rev": True},
        {"id": 45, "text": "Most people tend to get angry more quickly than I do.", "rev": False},
        {"id": 46, "text": "Most people are more upbeat and dynamic than I generally am.", "rev": True},
        {"id": 47, "text": "I feel strong emotions when someone close to me is going away for a long time.", "rev": False},
        {"id": 48, "text": "I want people to know that I am an important person of high status.", "rev": True},
        {"id": 49, "text": "I don't think of myself as the artistic or creative type.", "rev": True},
        {"id": 50, "text": "People often call me a perfectionist.", "rev": False},
        {"id": 51, "text": "Even when people make a lot of mistakes, I rarely say anything negative.", "rev": False},
        {"id": 52, "text": "I sometimes feel that I am a worthless person.", "rev": True},
        {"id": 53, "text": "Even in an emergency I wouldn't feel like panicking.", "rev": True},
        {"id": 54, "text": "I wouldn't pretend to like someone just to get that person to do favors for me.",
         "rev": False},
        {"id": 55, "text": "I find it boring to discuss philosophy.", "rev": True},
        {"id": 56, "text": "I prefer to do whatever comes to mind, rather than stick to a plan.", "rev": True},
        {"id": 57, "text": "When people tell me that I'm wrong, my first reaction is to argue with them.", "rev": True},
        {"id": 58, "text": "When I'm in a group of people, I'm often the one who speaks on behalf of the group.",
         "rev": False},
        {"id": 59, "text": "I remain unemotional even in situations where most people get very sentimental.",
         "rev": True},
        {"id": 60, "text": "I'd be tempted to use counterfeit money, if I were sure I could get away with it.",
         "rev": True},
    ]
    NUM_QUESTIONS = len(QUESTIONS_HEXACO)
    QUESTIONS_DICT = {q['id']: q for q in QUESTIONS_HEXACO}
    HONESTY_HUMILITY = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
    EMOTIONALITY = [5, 11, 17, 23, 29, 35, 41, 47, 53, 59]
    EXTRAVERSION = [4, 10, 16, 22, 28, 34, 40, 46, 52, 58]
    AGREEABLENESS = [3, 9, 15, 21, 27, 33, 39, 45, 51, 57]
    CONSCIENTIOUSNESS = [2, 8, 14, 20, 26, 32, 38, 44, 50, 56]
    OPENNESS_EXPERIENCE = [1, 7, 13, 19, 25, 31, 37, 43, 49, 55]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    score_honesty = models.FloatField()
    score_emotionality = models.FloatField()
    score_extraversion = models.FloatField()
    score_agreeableness = models.FloatField()
    score_conscientiousness = models.FloatField()
    score_openness = models.FloatField()

    def set_hexaco_scores(self):
        def get_val(idx):
            q = C.QUESTIONS_DICT[idx]
            raw_val = getattr(self, f'hexaco_{idx}')
            # Inversion si rev est True : (Max+1) - score
            return (6 - raw_val) if q['rev'] else raw_val

        # Calcul des moyennes pour chaque facteur
        self.score_honesty = sum(get_val(i) for i in C.HONESTY_HUMILITY) / 10
        self.score_emotionality = sum(get_val(i) for i in C.EMOTIONALITY) / 10
        self.score_extraversion = sum(get_val(i) for i in C.EXTRAVERSION) / 10
        self.score_agreeableness = sum(get_val(i) for i in C.AGREEABLENESS) / 10
        self.score_conscientiousness = sum(get_val(i) for i in C.CONSCIENTIOUSNESS) / 10
        self.score_openness = sum(get_val(i) for i in C.OPENNESS_EXPERIENCE) / 10


for q in C.QUESTIONS_HEXACO:
    setattr(Player, f"hexaco_{q['id']}", models.IntegerField(
        choices=[[1, '1'], [2, '2'], [3, '3'], [4, '4'], [5, '5']],
        widget=widgets.RadioSelectHorizontal,
        label=q["text"]
    ))


class Hexaco(Page):
    form_model = 'player'

    def get_form_fields(player):
        return [f'hexaco_{i}' for i in range(1, C.NUM_QUESTIONS + 1)]

    @staticmethod
    def js_vars(player: Player):
        return dict(fill_auto=player.session.config.get("fill_auto", False))

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            for q in range(1, C.NUM_QUESTIONS + 1):
                setattr(player, f"hexaco_{q}", random.randint(1, 5))
        player.set_hexaco_scores()


page_sequence = [Hexaco]
