# Maze game

# import the required modules
import pygame
import random

# define the size of the game window
WIDTH = 800
HEIGHT = 600

# define the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize the pygame module
pygame.init()

# create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Game")

# create the player sprite
player = pygame.image.load("player.png").convert()
player.set_colorkey(BLACK)
player_rect = player.get_rect()

# create the walls
wall_list = pygame.sprite.Group()

# create the coins
coin_list = pygame.sprite.Group()

# create the walls and coins
for i in range(10):
    # create a wall
    wall = pygame.image.load("wall.png").convert()
    wall.set_colorkey(BLACK)
    wall_rect = wall.get_rect()
    wall_rect.x = random.randrange(WIDTH)
    wall_rect.y = random.randrange(HEIGHT)
    wall_list.add(wall)

    # create a coin
    coin = pygame.image.load("coin.png").convert()
    coin.set_colorkey(BLACK)
    coin_rect = coin.get_rect()
    coin_rect.x = random.randrange(WIDTH)
    coin_rect.y = random.randrange(HEIGHT)
    coin_list.add(coin)

# game loop
running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # check if the player has collided with a wall
    hit_list = pygame.sprite.spritecollide(player, wall_list, False)
    if len(hit_list) > 0:
        print("You lose!")
        running = False

    # check if the player has collected a coin
    hit_list = pygame.sprite.spritecollide(player, coin_list, True)
    if len(hit_list) > 0:
        print("You win!")
        running = False
        
    # update the screen
    screen.fill(BLACK)
    screen.blit(player, player_rect)
    wall_list.draw(screen)
    coin_list.draw(screen)
    pygame.display.flip()

# quit the game
pygame.quit()
