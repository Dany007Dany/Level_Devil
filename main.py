import pygame
import sys
import math
from player import Player
pygame.init()
#CLOCK
clock = pygame.time.Clock()
#WINDOW SETTINGS
WIDTH = 64*20
HEIGHT  = 64*10
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("NINJA RUNNER")
icon = pygame.image.load("Ninja Images/Run__002.png").convert_alpha()
pygame.display.set_icon(icon)

#IMAGES
background = pygame.image.load("Map Images/BG/BG.png").convert_alpha()
background_width = background.get_width()
ground1 = pygame.image.load("Map Images/Tiles/2.png").convert_alpha()
ground1 = pygame.transform.scale(ground1, (64, 64))
ground1_width = ground1.get_width()
tiles_2 = math.ceil(WIDTH / ground1_width + 1)

#VARIABLES FOR SCROLLING EFFECT
key = pygame.key.get_pressed()
scroll = 0
scroll_2 = 0
tiles = math.ceil(WIDTH / background_width) + 1


#PLAYER AND BOTS
moving_sprites_player_idle = pygame.sprite.Group()
player = Player(200, (HEIGHT - 155))
moving_sprites_player_idle.add(player)


#STARTING DISPLAY




#MAIN LOOP
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()

    player.animate()
    player.apply_gravity()

    #SCROLLING BACKGROUND
    for i in range(0, tiles):
        screen.blit(background, (i * background_width + scroll,0))
    for i in range(0, tiles_2):
        screen.blit(ground1, (i * ground1_width + scroll_2, HEIGHT - 64))
    
    scroll -= 5
    scroll_2 -= 5
    #reset scroll
    if abs(scroll) > background_width:
        scroll = 0
    if abs(scroll_2) > ground1_width:
        scroll_2 = 0
    

    #PLAYER BLIT AND FUNCTIONS
    moving_sprites_player_idle.draw(screen)
    
    player.update()
    #SCREEN UPDATE
    pygame.display.update()
    pygame.display.flip()
    clock.tick(60)
