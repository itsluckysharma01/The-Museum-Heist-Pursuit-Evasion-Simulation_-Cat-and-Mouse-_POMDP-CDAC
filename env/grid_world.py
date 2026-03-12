import numpy as np

class GridWorld:

    ACTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

    def __init__(self, size=10):
        self.size = size

        # Impassable wall cells
        self.walls = {
            (1, 3), (2, 3), (3, 3),   # left barrier top
            (6, 3), (7, 3), (8, 3),   # left barrier bottom
            (1, 6), (2, 6), (3, 6),   # right barrier top
            (6, 6), (7, 6), (8, 6),   # right barrier bottom
        }

        # Door cells — visually distinct, but passable
        self.doors = {(4, 3), (5, 3), (4, 6), (5, 6)}

        # Museum exhibit objects
        self.objects = [(2, 1), (2, 5), (2, 8), (7, 1), (7, 5), (7, 8)]

        self.artifact = (8, 8)
        self.exit = (0, 9)

        self.reset()

    def reset(self):
        self.guard = [0, 0]
        self.intruder = [9, 9]
        return self.get_state()

    def get_state(self):
        return {
            "guard": self.guard,
            "intruder": self.intruder,
            "artifact": self.artifact,
            "exit": self.exit
        }

    def move(self, pos, action):
        x, y = pos

        if action == "UP":
            nx, ny = x - 1, y
        elif action == "DOWN":
            nx, ny = x + 1, y
        elif action == "LEFT":
            nx, ny = x, y - 1
        elif action == "RIGHT":
            nx, ny = x, y + 1
        else:
            nx, ny = x, y

        nx = max(0, min(self.size - 1, nx))
        ny = max(0, min(self.size - 1, ny))

        # Block movement into walls (doors are passable)
        if (nx, ny) in self.walls:
            return [x, y]

        return [nx, ny]