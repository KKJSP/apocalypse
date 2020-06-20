import pygame
from vector import Vector
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, BACKGROUND, PLAYER


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.speed = 10
        self.pos = Vector(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

        self.surf = pygame.Surface((10, 10))
        self.rect = self.surf.get_rect(center=self.pos.tuple())
        self.surf.fill(COLORS[BACKGROUND])
        pygame.draw.circle(self.surf, COLORS[PLAYER], (5, 5), 5)

    def update(self, pressed_keys):
        mouse_pos = Vector(*pygame.mouse.get_pos())
        direction = mouse_pos - self.pos
        move_vector = direction.asint()
        self.pos += move_vector
        self.rect.move_ip(move_vector.x, move_vector.y)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
