import numpy as np

class Particle:
    def __init__(self, N, Xmin, Xmax):
        self.x = np.random.rand(1, N)
        self.vel = 0
        self.best_pos = None
        self.neighbour = np.array([None, None])
        self.current_fit = None
        self.best_fit = None

