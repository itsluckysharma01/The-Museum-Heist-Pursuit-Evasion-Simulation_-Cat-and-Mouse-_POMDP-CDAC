import numpy as np

class BeliefState:

    def __init__(self, grid_size):

        self.grid_size = grid_size
        self.belief = np.ones((grid_size,grid_size))
        self.belief /= self.belief.sum()

    def update(self, observation):

        if observation:

            self.belief *= 1.2
        else:
            self.belief *= 0.9

        self.belief /= self.belief.sum()

    def most_likely_position(self):

        idx = np.argmax(self.belief)

        x = idx // self.grid_size
        y = idx % self.grid_size

        return [x,y]