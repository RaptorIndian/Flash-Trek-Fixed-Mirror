import pygame
import math
import threading
import Weapons


class Player(pygame.sprite.Sprite):

    def __init__(self, pos=(0, 0)):
        super(Player, self).__init__()
        self.original_image = pygame.image.load("./images/Danube_Runabout.png").convert()
        self.image = self.original_image  # This will reference our rotated image.
        self.rect = self.image.get_rect().move(pos)
        self.angle = 0
        self.speed = 0

    def update(self):
        self.image = pygame.transform.rotate(self.original_image, self.angle)
        x, y = self.rect.center  # Save its current center.
        if self.speed > 0:
            # Create a thread to move the player forward continuously.
            t = threading.Thread(target=self.move_forward)
            t.start()
        self.rect = self.image.get_rect()  # Replace old rect with new rect.
        self.rect.center = (x, y)  # Put the new rect's center at old center.

        # Check if the player is pressing a key.
        key = pygame.key.get_pressed()

        # If the player is pressing the left key, rotate the player left.
        if key[pygame.K_LEFT]:
            self.angle += 1 % 360  # Value will repeat after 359. This prevents angle to overflow.

        # If the player is pressing the right key, rotate the player right.
        if key[pygame.K_RIGHT]:
            self.angle -= 1 % 360

        # If the player is pressing the up key, increase the player's speed.
        if key[pygame.K_UP]:
            # If the player's speed is less than 10.
            if self.speed < 10:
                self.speed += 1
            print(self.speed)
        
        # If the player is pressing the down key, decrease the player's speed.
        if key[pygame.K_DOWN]:
            # If the player's speed is greater than 0.
            if self.speed > 0:
                self.speed -= 1
            print(self.speed)

    def move_forward(self):
        # Calculate the new position of the player based on the angle and speed
        radians = math.radians(self.angle)
        dx = self.speed * math.cos(radians)
        dy = self.speed * math.sin(radians)
        self.rect.x += dx
        self.rect.y -= dy

        return dx, dy

    def create_bullet(self):
        # Get the center of the player sprite.
        center_x, center_y = self.rect.center

        # Spawn a bullet in the direction the player is facing.
        return Weapons.Bullet(center_x, center_y, self.angle, 2, 2, 10, 200, 200)