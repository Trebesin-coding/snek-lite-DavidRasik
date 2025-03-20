import pygame
import random
from sys import exit


pygame.init()


screen_height = 600
screen_width = 800


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()


running = True


player_x = 150
player_y = 150
player_size = 30
player_speed = 10


player_rect = pygame.Rect(player_x, player_y, player_size, player_size)


score = 0


font = pygame.font.Font(None, 30)


coin_size = 20
coin_color = (255, 0, 0)
coin_rect = pygame.Rect(random.randint(0, screen_width - coin_size), random.randint(0, screen_height - coin_size), coin_size, coin_size)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w]:
        player_rect.y -= player_speed
    if keys[pygame.K_s]:
        player_rect.y += player_speed
    if keys[pygame.K_a]:
        player_rect.x -= player_speed
    if keys[pygame.K_d]:
        player_rect.x += player_speed


    if player_rect.colliderect(coin_rect):
        score += 1
        coin_rect.x = random.randint(0, screen_width - coin_size)
        coin_rect.y = random.randint(0, screen_height - coin_size)


    screen.fill((255, 255, 255))


    pygame.draw.rect(screen, (0, 0, 255), player_rect)


    pygame.draw.rect(screen, coin_color, coin_rect)


    score_text = font.render(f'Skore: {score}', True, (0, 0, 0))
    screen.blit(score_text, (screen_width - 150, 10))


    pygame.display.update()
    clock.tick(60)
