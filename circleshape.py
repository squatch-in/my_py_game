import pygame
# from player import Player

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

#calc the distance between 2 circles

    def colision_detect(self, other_circle): 
        distance = self.position.distance_to(other_circle.position)
        sum = self.radius + other_circle.radius
        return (distance <= sum)
