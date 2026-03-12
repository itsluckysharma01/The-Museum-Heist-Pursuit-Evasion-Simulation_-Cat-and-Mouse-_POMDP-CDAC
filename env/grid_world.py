import numpy as np

class GridWorld:

    def __init__(self, size=10):
        self.size = size
        self.reset()

    def reset(self):
        self.guard_pos = [0,0]
        self.intruder_pos = [9,9]

        self.artifact = [8,8]
        self.exit = [0,9]

        return self.get_state()

    def get_state(self):
        return {
            "guard": self.guard_pos,
            "intruder": self.intruder_pos,
            "artifact": self.artifact,
            "exit": self.exit
        }

    def move(self, pos, action):

        x,y = pos

        if action == "UP":
            x -= 1
        elif action == "DOWN":
            x += 1
        elif action == "LEFT":
            y -= 1
        elif action == "RIGHT":
            y += 1

        x = max(0, min(self.size-1, x))
        y = max(0, min(self.size-1, y))

        return [x,y]