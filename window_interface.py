import pygame
from pygame.locals import*
from constant import *
from labyrinth import *

pygame.init()

#Open pygame surface
window_surface = pygame.display.set_mode(window_resolution)
#title
pygame.display.set_caption(title)

#Load pictures

black_ground = pygame.image.load(black_ground_pic)
home_pic = pygame.image.load(home_pic)
start_button = pygame.image.load(start_button)
restart_button = pygame.image.load(restart_button)
quit_button = pygame.image.load(quit_button)
quit_button_game = pygame.image.load(quit_button_game)
background_pic = pygame.image.load(background_pic)
wall_pic = pygame.image.load(wall_pic)
player_pic = pygame.image.load(player_pic)
gardian_pic = pygame.image.load(gardian_pic)

syringe_pic = pygame.image.load(syringe_pic).convert()
needle_pic = pygame.image.load(needle_pic).convert()
ether_pic = pygame.image.load(ether_pic).convert()

labyrinth = Create_game()
labyrinth = labyrinth.labyrinth.labyrinth





#Main loop
run_display = 1
while run_display:
    
    
    display_home = 1
    display_game = 1

    #Home loop
    while display_home == 1:
        window_surface.blit(black_ground, [0, 0])
        window_surface.blit(home_pic, [1,0])
        window_surface.blit(start_button, [293, 62])
        window_surface.blit(quit_button, [28,62])

        pygame.display.flip()
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
		
            elif event.type == KEYDOWN:
                display_home = 0
    
    #Game loop
    while display_game == 1:
        
        window_surface.blit(black_ground, [0, 0])
        window_surface.blit(restart_button, [8, 455])
        window_surface.blit(quit_button_game, [5, 490])
        window_surface.blit(background_pic, [0,0])
        
        window_surface.blit(player_pic, [0, 0])
        window_surface.blit(gardian_pic, [14*sprite_cote, 14*sprite_cote])
        
        
        line_nbr = 0
        for line in labyrinth:
            column_nbr = 0
            for sprite in line:
                x = column_nbr * sprite_cote
                y = line_nbr * sprite_cote

                if sprite == 'w':
                    window_surface.blit(wall_pic, [x, y])
                if sprite == 'E':
                    window_surface.blit(ether_pic, [x, y])
                if sprite == 'N':
                    window_surface.blit(needle_pic, [x, y])
                if sprite == 'S':
                    window_surface.blit(syringe_pic, [x, y])
                
                column_nbr += 1
            line_nbr += 1

        pygame.time.Clock().tick(30)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == QUIT:
                display_game = 0
                display_home = 0
            

         
                

