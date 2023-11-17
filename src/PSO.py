
from particle import Particle
import numpy as np
from multiprocessing import Pool

class ParticleSwarmOptimization:
    def __init__(self, Vmin, Vmax, Xmin, Xmax, Ngenerations, Nparticles, N, pop, fitness, c1=0, c2=0):
        self.c1 = c1
        self.c2 = c2
        self.phi = self.c1+self.c2
        self.chi = 2/abs(2 - self.phi - np.sqrt(self.phi**2 - 4*self.phi))
        self.particles = self.__create_particles(Xmin, Xmax, Nparticles, N, pop)
        self.bestparticle = None
        self.gen = 0
        pass
    
    def __create_particles(self, Xmin, Xmax, Nparticles, N, pop):
        particles = list([Particle(N, Xmin, Xmax) for i in range(pop)])

        for particle in particles:
            index = particles.index(particle)
            
            # first neighbour
            try: 
                particle.neighbour[0] = particles[index + 1]
            except IndexError:
                pass
            
            # second neighbour
            if index:        
                particle.neighbour[1] = particles[index - 1]
        
        self.bestparticle = particles[0]
        self.gen = 1
            
        return particles
    
    def __run_generation(self, fitness):
        for particle in self.particles:
            particle.currentFit = fitness(particle)
        
        self.gen+=1
        pass

opti1 = ParticleSwarmOptimization(Vmin=1, Vmax=2, Xmin=1, Xmax=2, Ngenerations=3, Nparticles=4, N=5, pop=5, fitness=2, c1=0, c2=0)
