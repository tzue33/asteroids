import pygame
from circleshape import *  # Adjust this import if CircleShape is defined elsewhere
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # Initialize the parent CircleShape with x, y, and radius.
        super().__init__(x, y, radius)
        # (Assuming CircleShape already sets up self.position and self.velocity)

    def draw(self, screen):
        # Draw the asteroid as a circle outline using white color and a width of 2.
        # Convert the position (a Vector2) into a tuple of integers.
        pos = (int(self.position.x), int(self.position.y))
        pygame.draw.circle(screen, "white", pos, int(self.radius), 2)

    def update(self, dt):
        # Move the asteroid in a straight line at constant speed.
        # Add (self.velocity * dt) to its position.
        self.position += self.velocity * dt

    def split(self):
        self.kill()  # Immediately remove this asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # If it's already small, do nothing further
        random_angle = random.uniform(20, 50)  # NEW: Random angle between 20 and 50 degrees
        # Create two new velocity vectors by rotating the current velocity
        new_velocity1 = self.velocity.rotate(random_angle) * 1.2  # Scale up by 1.2
        new_velocity2 = self.velocity.rotate(-random_angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS  # NEW: Compute the new, smaller radius
        # Spawn two new asteroids at the same position with the new radius
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_velocity2
