import pygame
import random

from vector import Vector
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, BACKGROUND, ENEMY


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((15, 15))
        self.surf.fill(COLORS[BACKGROUND])
        pygame.draw.circle(self.surf, COLORS[ENEMY], (7, 7), 7)
        pygame.draw.circle(self.surf, (255, 255, 255), (7, 7), 7, 1)

        pos = random.randint(0, 3)
        if pos == 0:
            x = random.randint(0, SCREEN_WIDTH)
            y = -20
        elif pos == 1:
            x = random.randint(0, SCREEN_WIDTH)
            y = SCREEN_HEIGHT + 20
        elif pos == 2:
            x = -20
            y = random.randint(0, SCREEN_HEIGHT)
        else:
            x = SCREEN_WIDTH + 20
            y = random.randint(0, SCREEN_HEIGHT)

        self.rect = self.surf.get_rect(center=(x, y))
        self.speed = random.randint(3, 4)
        self.pos = Vector(x, y)
        self.lived = False

    def update(self, player):
        move_vector = (player.pos - self.pos).normalized() * self.speed
        move_vector = move_vector.asint()
        self.pos += move_vector
        self.rect.move_ip(move_vector.x, move_vector.y)

        if self.lived:
            if self.rect.right < 0 or self.rect.right > SCREEN_WIDTH:
                self.kill()
        else:
            if self.rect.right > 0 and self.rect.right < SCREEN_WIDTH:
                self.lived = True
