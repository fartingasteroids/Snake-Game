import pygame
import time
import random

pygame.init()

ROW = 25
COL = ROW
TILE_SIZE = 25
WIDTH = TILE_SIZE * COL
HEIGHT = TILE_SIZE * ROW
WIN =pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

def get_random(limit):
    return random.randint(0, limit-1) * TILE_SIZE

def main():
    run = True

    food = pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE)
    player = [] 
    player.append(pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE))
    snake_velocity = (0, 0)

    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break 
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake_velocity = (0, -TILE_SIZE)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake_velocity = (0, +TILE_SIZE)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake_velocity = (-TILE_SIZE, 0)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake_velocity = (+TILE_SIZE, 0)

        for i in range(len(player)-1, 0, -1):
            player[i] = player[i-1].copy()
        
        player[0].move_ip(snake_velocity)

        for part in player[1:]:
            if player[0].center == part.center:
                player.clear()
                food = pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE)
                player.append(pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE))

        if player[0].center == food.center:
            player.append(food)
            food = pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE)
        
        if not WIN.get_rect().contains(player[0]):
            player.clear()
            food = pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE)
            player.append(pygame.Rect(get_random(COL), get_random(ROW), TILE_SIZE, TILE_SIZE))


        WIN.fill("black")
        pygame.draw.rect(WIN, "red", food)
        
        for part in player:
            pygame.draw.rect(WIN, "green", part)

        pygame.display.update()     
        clock.tick(10)  
    
    pygame.quit()

if __name__ == "__main__":
    main()