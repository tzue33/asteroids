from constants import *
from circleshape import *
from shot import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.position = pygame.Vector2(x, y)
        self.rotation = 0
        self.shoot_timer = 0  # NEW: Timer for shooting cooldown

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # Create a unit vector pointing up and rotate it by the current rotation.
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        # Move the player's position by the scaled vector.
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):  # NEW: Method to spawn a shot
        shot = Shot(self.position.x, self.position.y)
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        shot.velocity = forward * PLAYER_SHOOT_SPEED
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN

    # Update method checks for key presses to rotate the player.
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            # Rotate left: use negative dt.
            self.rotate(-dt)
        if keys[pygame.K_d]:
            # Rotate right: use positive dt.
            self.rotate(dt)
        if keys[pygame.K_w]:
            # Move forward.
            self.move(dt)
        if keys[pygame.K_s]:
            # Move backward by reversing dt.
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()

        self.shoot_timer = max(0, self.shoot_timer - dt)

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), 2)