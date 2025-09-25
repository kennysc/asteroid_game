from circleshape import CircleShape
import pygame
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white", self.position, self.radius, 2)

    def update(self, dt):
       self.position += self.velocity * dt 

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20, 50)
            velo_1 = self.velocity.rotate(angle)
            velo_2 = self.velocity.rotate(-angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            aste_1 = Asteroid(self.position.x, self.position.y, new_radius)
            aste_2 = Asteroid(self.position.x, self.position.y, new_radius)
            aste_1.velocity = velo_1 * 1.2
            aste_2.velocity = velo_2 * 1.2

