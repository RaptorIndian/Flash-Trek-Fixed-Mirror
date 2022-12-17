import pygame


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

        if self.rect.right < (0 - 100) or self.rect.left > pygame.display.get_surface().get_width() + 100 or self.rect.top > pygame.display.get_surface().get_height() + 100 or self.rect.bottom < (0 - 100):
            self.kill()
            