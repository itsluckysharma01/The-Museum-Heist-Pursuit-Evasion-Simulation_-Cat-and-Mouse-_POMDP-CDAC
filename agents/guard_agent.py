import random

class GuardAgent:

    ACTIONS = ["UP","DOWN","LEFT","RIGHT"]

    def __init__(self, belief):

        self.belief = belief

    def choose_action(self):

        target = self.belief.most_likely_position()

        return random.choice(self.ACTIONS)