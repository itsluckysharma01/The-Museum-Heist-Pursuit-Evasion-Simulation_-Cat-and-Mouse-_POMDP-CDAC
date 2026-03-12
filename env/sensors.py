import random

class MotionSensor:

    def __init__(self, false_positive=0.1, false_negative=0.2):
        self.fp = false_positive
        self.fn = false_negative

    def detect(self, guard_pos, intruder_pos):

        if guard_pos == intruder_pos:

            if random.random() < self.fn:
                return False

            return True

        else:

            if random.random() < self.fp:
                return True

            return False