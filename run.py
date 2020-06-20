# Import the pygame module
import pygame
from pygame.locals import QUIT

from player import Player
from enemy import Enemy
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS, BACKGROUND

pygame.init()
pygame.mouse.set_visible(False)

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

player = Player()
enemies = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(player)

clock = pygame.time.Clock()

running = True

while running:
    pressed_keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    screen.fill(COLORS[BACKGROUND])

    player.update(pressed_keys)
    enemies.update(player)

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    pygame.display.flip()

    clock.tick(30)
