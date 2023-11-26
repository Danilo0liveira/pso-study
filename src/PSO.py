
from particle import Particle
import numpy as np
from multiprocessing import cpu_count
import concurrent.futures

class ParticleSwarmOptimization:
    def __init__(self, Vmin, Vmax, Xmin, Xmax, Ngenerations, N, pop, fitness, c1=0, c2=0):
        self.fitness = fitness
        self.c1 = c1
        self.c2 = c2
        self.phi = self.c1+self.c2
        self.chi = 2/abs(2 - self.phi - np.sqrt(self.phi**2 - 4*self.phi))
        self.particles = self.__create_particles(Xmin, Xmax, N, pop)
        self.best_particle = None
        self.gen = 0
        self.Vmin = Vmin
        self.Vmax = Vmax
        self.Xmax = Xmax    
        self.Xmin = Xmin
        
        pass
    
    def __create_particles(self, Xmin, Xmax, N, pop):
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
        
        self.best_particle = particles[0]
        self.gen = 1
            
        return particles
    
    def set_particle_current_fit(self, particle):
        particle.current_fit = self.fitness(particle)
        
        # biggest value optimization
        
        if particle.best_fit == None:
            particle.best_fit = np.copy(particle.current_fit)
            particle.best_pos = np.copy(particle.x)
            
        if abs(particle.current_fit) < abs(particle.best_fit):
            particle.best_fit = np.copy(particle.current_fit)
            particle.best_pos = np.copy(particle.x)
        pass
    
    def run_generation(self):
        
        # with concurrent.futures.ProcessPoolExecutor(max_workers=cpu_count()) as executor:
                # executor.map(self.set_particle_current_fit, self.particles)

        for particle in self.particles:
            self.set_particle_current_fit(particle)

        self.best_particle = sorted(self.particles, key= lambda p : p.best_fit)[0] 
        self.gen+=1

        self.__uptdate_positions()
        pass
    
    def __uptdate_positions(self,):
        for particle in self.particles:
            eps1 = np.random.rand()
            eps2 = np.random.rand()

            lock_neighbour = particle.neighbour[particle.neighbour != None]

            if len(lock_neighbour) > 1:
                lock_neighbour = min(particle.neighbour[0].best_fit, particle.neighbour[0].best_fit)
            else:
                lock_neighbour =  lock_neighbour[0].best_fit

            particle.vel = self.c1 * eps1 * (particle.best_pos - particle.x)
            particle.vel += self.c2 * eps2 * (lock_neighbour - particle.x)
            
            particle.vel[particle.vel > self.Vmax] = self.Vmax
            particle.vel[particle.vel < self.Vmin] = self.Vmin
            
            particle.x += particle.vel
            
            particle.x[particle.x > self.Xmax] = self.Xmax
            particle.x[particle.x < self.Xmin] = self.Xmin
        pass
