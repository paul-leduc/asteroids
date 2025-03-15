from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, SHOT_RADIUS)
        self.x = x
        self.y = y
        self.radius = SHOT_RADIUS
        self.velocity = pygame.Vector2(0, 1)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, 2)
    
    def update(self, dt):
        self.position += super().get_velocity() * dt


