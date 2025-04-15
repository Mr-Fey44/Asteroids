import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        # randomize the angle of the split
        random_angle = random.uniform(20, 50)
        v1 = self.velocity.rotate(random_angle) * 1.2
        v2 = self.velocity.rotate(-random_angle) * 1.2
        new_asteroids = [
            Asteroid(self.position.x, self.position.y, new_radius),
            Asteroid(self.position.x, self.position.y, new_radius)
        ]
        new_asteroids[0].velocity = v1
        new_asteroids[1].velocity = v2
        return new_asteroids
