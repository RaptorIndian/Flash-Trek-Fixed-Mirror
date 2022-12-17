import pygame
import sys
import time
import Weapons, Entities

# Basics
pygame.init()
clock = pygame.time.Clock()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

player = Entities.Player()
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