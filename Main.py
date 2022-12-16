import pygame
import sys
import time


class Player(pygame.sprite.Sprite):
    def __init__(self):

        pygame.sprite.Sprite.__init__(self)
        # Load the image and create a mask from it
        self.image = pygame.image.load("./images/Danube_Runabout.png").convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width / 2, screen_height / 2)
        self.direction = "up"

    def update(self):
        
        # If the player holds any of the arrow keys, move the player
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.direction = "up"
            self.rect.y -= 5
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.direction = "down"
            self.rect.y += 5
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.direction = "left"
            self.rect.x -= 5
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.direction = "right"
            self.rect.x += 5

    def create_bullet(self):
        return Bullet(self.rect.centerx, self.rect.centery, self.direction)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.direction = direction 
        self.speed = 10

    def update(self):

        if self.direction == "up":
            self.image = pygame.Surface((5, 25))
            self.image.fill((0, 200, 0))
            self.y -= self.speed
        elif self.direction == "down":
            self.image = pygame.Surface((5, 25))
            self.image.fill((0, 200, 0))
            self.y += self.speed
        elif self.direction == "left":
            self.image = pygame.Surface((25, 5))
            self.image.fill((0, 200, 0))
            self.x -= self.speed
        elif self.direction == "right":
            self.image = pygame.Surface((25, 5))
            self.image.fill((0, 200, 0))
            self.x += self.speed

        self.rect.center = (self.x, self.y)

        if self.rect.right < (0 - 100) or self.rect.left > screen_width + 100 or self.rect.top > screen_height + 100 or self.rect.bottom < (0 - 100):
            self.kill()


# Basics
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

player = Player()
player_group = pygame.sprite.Group()
player_group.add(player)

bullet_group = pygame.sprite.Group()

last_bullet_time = time.time()

while True:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # If keydown event is space, create a bullet
        if event.type == pygame.KEYDOWN:
            # If the player presses space and the user event is not already firing
            if event.key == pygame.K_SPACE:
                
                # Generate a bullet.
                bullet = player.create_bullet()

                # Save the current time.
                current_time = time.time()
                
                time_since_last_bullet = current_time - last_bullet_time

                # Check if the bullet can fire again.
                if time_since_last_bullet >= 0.5:
                    bullet_group.add(bullet)
                    last_bullet_time = time.time()
            
                

            

    # Drawing
    screen.fill((0, 0, 0))
    bullet_group.draw(screen)
    bullet_group.update()
    player_group.draw(screen)
    player_group.update()
    pygame.display.flip()