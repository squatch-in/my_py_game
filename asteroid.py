from os.path import split

import pygame
import random

from pygame.transform import rotate

from circleshape import CircleShape
from constants import*

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)


    def draw(self, screen):
        pygame.draw.circle(surface=screen, color="white", center=(self.position.x, self.position.y), radius=self.radius, width=2)
    
    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
             print("this was a small asteroid")
        else:
            random_angle = random.uniform(20, 50)

            velocity1 = pygame.Vector2.rotate(self.velocity, random_angle) * 1.2
            velocity2 = pygame.Vector2.rotate(self.velocity, -random_angle) * 1.2
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            first = Asteroid(self.position, self.position, new_radius)
            second = Asteroid(self.position, self.position, new_radius)
            first.velocity += (velocity1 * 1.2)
            second.velocity -= (velocity2 * 1.2)



