import pygame
from pygame.locals import *
from constant import *
from labyrinth import *

class GameInterface():


    def __init__(self):
        
        labyrinth = Create_game()
        self.labyrinth = labyrinth.labyrinth.labyrinth


        self.create_surface()
        self.load_images()
        self.rect_position()
        self.window_display()


    def create_surface (self):

        pygame.display.init()
        pygame.display.set_caption(title)
        self.window_surface = pygame.display.set_mode(window_resolution)
    
    def load_images(self):

        self.home_pic = pygame.image.load(home_pic)
        self.start_button = pygame.image.load(start_button)
        self.quit_button = pygame.image.load(quit_button)

        self.background_pic = pygame.image.load(background_pic)
        self.restart_button = pygame.image.load(restart_button)
        self.quit_button_game = pygame.image.load(quit_button_game)
        self.player_pic = pygame.image.load(player_pic)
        self.gardian_pic = pygame.image.load(gardian_pic).convert()
        self.gardian_pic.set_colorkey(white_color)


        self.wall_pic = pygame.image.load(wall_pic)

        self.syringe_pic = pygame.image.load(syringe_pic).convert()
        self.syringe_pic.set_colorkey(white_color)
        self.syringe_pic_menu = pygame.image.load(syringe_pic_menu).convert()
        self.syringe_pic_menu.set_colorkey(white_color)

        self.dropper_pic = pygame.image.load(dropper_pic).convert()
        self.dropper_pic.set_colorkey(white_color)
        self.dropper_pic_menu = pygame.image.load(dropper_pic_menu).convert()
        self.dropper_pic_menu.set_colorkey(white_color)

        self.tube_pic = pygame.image.load(tube_pic).convert()
        self.tube_pic.set_colorkey(white_color)
        self.tube_pic_menu = pygame.image.load(tube_pic_menu).convert()
        self.tube_pic_menu.set_colorkey(white_color)

        self.croco_pic = pygame.image.load(croco_pic).convert()
        self.croco_pic.set_colorkey(white_color)

        self.heart_pic = pygame.image.load(heart_pic).convert()
        self.heart_pic.set_colorkey(white_color)

        
    def rect_position(self):
    
        self.start_rect = pygame.Rect((293, 62), (130, 126))
        self.quit_rect = pygame.Rect((28, 62), (130, 126))

        self.restart_rect = pygame.Rect((5, 456), (180, 25))
        self.quit_game_rect = pygame.Rect((5, 490), (180, 25))
    
    
    def window_display(self):
   
        run_display = 1
        while run_display == 1:

            run_home = 1
            run_game = 1

            while run_home == 1:
                pygame.time.Clock().tick(30)
                self.window_surface.blit(self.home_pic, [0,0])
                self.window_surface.blit(self.start_button, [293, 62])
                self.window_surface.blit(self.quit_button, [28, 62])
                
                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit()

                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.quit_rect.collidepoint(event.pos):
                                quit()
                            if self.start_rect.collidepoint(event.pos):
                                run_home = 0
                                
                
            while run_game == 1:

                pygame.time.Clock().tick(30)
                self.window_surface.fill(black_color)
                self.window_surface.blit(self.restart_button, [5, 456])
                self.window_surface.blit(self.quit_button_game, [5, 490])
                self.window_surface.blit(self.background_pic, [0,0])
                    
                self.window_surface.blit(self.player_pic, [0, 0])
                self.window_surface.blit(self.gardian_pic, [14*sprite_cote, 14*sprite_cote])
                    
                self.window_surface.blit(self.syringe_pic_menu, (7*sprite_cote, 16*sprite_cote))
                self.window_surface.blit(self.dropper_pic_menu, (8*sprite_cote, 16*sprite_cote))
                self.window_surface.blit(self.tube_pic_menu, (9*sprite_cote, 16*sprite_cote))
                self.window_surface.blit(self.heart_pic, (13*sprite_cote, 16*sprite_cote))
                self.window_surface.blit(self.heart_pic, (11*sprite_cote, 16*sprite_cote))
                
                
                line_nbr = 0
                for line in self.labyrinth:
                    column_nbr = 0
                    for sprite in line:
                        x = column_nbr * sprite_cote
                        y = line_nbr * sprite_cote

                        if sprite == 'w':
                            self.window_surface.blit(self.wall_pic, [x, y])
                        if sprite == 'T':
                            self.window_surface.blit(self.tube_pic, [x, y])
                        if sprite == 'D':
                            self.window_surface.blit(self.dropper_pic, [x, y])
                        if sprite == 'S':
                            self.window_surface.blit(self.syringe_pic, [x, y])
                        if sprite == "C":
                            self.window_surface.blit(self.croco_pic, [x, y])
                        
                        column_nbr += 1
                    line_nbr += 1

                pygame.display.flip()

                for event in pygame.event.get():
                    if event.type == QUIT:
                        quit()

                    elif event.type == MOUSEBUTTONDOWN:
                        if event.button == 1:
                            if self.restart_rect.collidepoint(event.pos):
                                run_game = 0
                                run_home = 1
                               
                            if self.quit_game_rect.collidepoint(event.pos):
                                run_game = 0
                    
                    """elif event.type == KEYDOWN:
                        if event.key == K_RIGHT:
                            self.player_movement = 'r'
                            """

GameInterface()
