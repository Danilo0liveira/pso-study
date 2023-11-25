import numpy as np

class Particle:
    def __init__(self, N, Xmin, Xmax):
        self.x = np.random.rand(1, N)
        self.vel = 0
        self.best_pos = self.x
        self.neighbour = [None, None]
        self.current_fit = 0
        self.best_fit = 0

