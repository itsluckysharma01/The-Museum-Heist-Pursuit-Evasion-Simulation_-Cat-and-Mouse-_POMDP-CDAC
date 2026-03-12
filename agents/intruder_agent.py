import random

class IntruderAgent:

    ACTIONS = ["UP","DOWN","LEFT","RIGHT"]

    def choose_action(self):

        return random.choice(self.ACTIONS)