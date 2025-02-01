# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys 
from constants import *
from player import *
from asteroid import *
from asteroidfield import AsteroidField
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatables = pygame.sprite.Group()  # All objects that can be updated
    drawables = pygame.sprite.Group()   # All objects that can be drawn
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()  # NEW: Group for shots

    Asteroid.containers = (asteroids, updatables, drawables)
    Player.containers = (updatables, drawables)
    AsteroidField.containers = (updatables,)
    Shot.containers = (shots, updatables, drawables)

    # Instantiate a Player in the middle of the screen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the 'updatables' group.
        updatables.update(dt)

        # NEW: Check for collisions between each asteroid and each shot.
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  # Use split() instead of kill() to handle splitting logic
                    shot.kill()

        # Clear the screen.
        screen.fill((0, 0, 0))

        # Draw all objects in the 'drawables' group.
        for sprite in drawables:
            sprite.draw(screen)
        pygame.display.flip()

        # Pause until 1/60th of a second has passed and update dt (in seconds)
        dt = clock.tick(60) / 1000.0

if __name__ == "__main__":
        
    main()