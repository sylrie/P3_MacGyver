import pygame
from pygame.locals import *
import player



class Game():

    def __init__(self):

        self.sprite_cote = 30
        
        # From Class Player()
        self.player = player.Player()
        self.labyrinth = self.player.labyrinth
        self.inventory = self.player.inventory
        self.health = self.player.health
        self.run = self.player.run

        self.create_surface()
        self.load_images()
        self.create_rect()
        self.display()
    
    def create_surface(self):

        pygame.init()
        pygame.display.set_caption("MacGyver Labyrinth")
        self.window_surface = pygame.display.set_mode((450, 520))

    def load_images(self):

        # Player's image
        self.player_pic = pygame.image.load("resources/images/player.png").convert()
        self.player_pic.set_colorkey((255, 255, 255))
        # Gardian's image
        self.gardian_pic = pygame.image.load("resources/images/gardian.png").convert()
        self.gardian_pic.set_colorkey((255, 255, 255))
        # Wall
        self.wall_pic = pygame.image.load("resources/images/wall.png")
        # Passage
        self.pass_pic = pygame.image.load("resources/images/pass.png")

        # Inventory
        self.inventory_pic = pygame.image.load("resources/images/inventory.png").convert()

        # Syringe's images
        self.syringe_pic = pygame.image.load("resources/images/syringe.png").convert()
        self.syringe_pic.set_colorkey((255, 255, 255))
        self.syringe_pic_menu = pygame.image.load("resources/images/syringe2.png").convert()
        self.syringe_pic_menu.set_colorkey((255, 255, 255))

        # Dropper's images
        self.dropper_pic = pygame.image.load("resources/images/dropper.png").convert()
        self.dropper_pic.set_colorkey((255, 255, 255))
        self.dropper_pic_menu = pygame.image.load("resources/images/dropper2.png").convert()
        self.dropper_pic_menu.set_colorkey((255, 255, 255))

        # Tube's images
        self.tube_pic = pygame.image.load("resources/images/tube.png").convert()
        self.tube_pic.set_colorkey((255, 255, 255))
        self.tube_pic_menu = pygame.image.load("resources/images/tube2.png").convert()
        self.tube_pic_menu.set_colorkey((255, 255, 255))

        # Fire's image
        self.fire_pic = pygame.image.load("resources/images/fire.png").convert()
        self.fire_pic.set_colorkey((255, 255, 255))

        # heart's images
        self.heart_pic = pygame.image.load("resources/images/heart.png").convert()
        self.heart_pic.set_colorkey((255, 255, 255))
        self.heart_pic_menu = pygame.image.load("resources/images/heart2.png").convert_alpha()
        self.heart_pic_menu.set_colorkey((255, 255, 255))
        
        # buttons
        self.restart_button = pygame.image.load("resources/images/restart.png")
        self.quit_button_game = pygame.image.load("resources/images/game_quit.png")
   
    def create_rect(self):

        self.restart_rect = pygame.Rect((5, 456), (180, 25))
        self.quit_game_rect = pygame.Rect((5, 490), (180, 25))

    def display(self):
    
        while self.run == "game":
            
            pygame.time.Clock().tick(30)
            
            self.run = self.player.run
            self.health = self.player.health

            # Display buttons
            self.window_surface.blit(self.restart_button, [5, 456])
            self.window_surface.blit(self.quit_button_game, [5, 490])
              
            # Display life
            if self.health == 0:
                self.window_surface.blit(self.heart_pic_menu, (13*self.sprite_cote, 16*self.sprite_cote))
                self.window_surface.blit(self.heart_pic_menu, (12*self.sprite_cote, 16*self.sprite_cote))
            if self.health == 1:
                self.window_surface.blit(self.heart_pic, (13*self.sprite_cote, 16*self.sprite_cote))
                self.window_surface.blit(self.heart_pic_menu, (12*self.sprite_cote, 16*self.sprite_cote))
            if self.health == 2:
                self.window_surface.blit(self.heart_pic, (12*self.sprite_cote, 16*self.sprite_cote))
                self.window_surface.blit(self.heart_pic, (13*self.sprite_cote, 16*self.sprite_cote))
            
            # Display inventory
            self.window_surface.blit(self.inventory_pic, [205, 455]) 
            if "dropper" in self.inventory:
                self.window_surface.blit(self.dropper_pic, (8*self.sprite_cote, 16*self.sprite_cote))
            if "syringe" in self.inventory:
                self.window_surface.blit(self.syringe_pic, (9*self.sprite_cote, 16*self.sprite_cote))
            if "tube" in self.inventory:
                self.window_surface.blit(self.tube_pic, (7*self.sprite_cote, 16*self.sprite_cote))

            # Display labytinth
            line_nbr = 0
            for line in self.labyrinth:
                column_nbr = 0
                for sprite in line:
                    x = column_nbr * self.sprite_cote
                    y = line_nbr * self.sprite_cote
                    if sprite != "w":
                        self.window_surface.blit(self.pass_pic, [x, y])
                    if sprite == "a":
                        self.window_surface.blit(self.gardian_pic, [x, y])
                    if sprite == 'w':
                        self.window_surface.blit(self.wall_pic, [x, y])
                    if sprite == "f":
                        self.window_surface.blit(self.fire_pic, [x, y])
                    if sprite == "H":
                        self.window_surface.blit(self.heart_pic, [x, y])
                    if sprite == 'T':
                        self.window_surface.blit(self.tube_pic, [x, y])
                    if sprite == 'D':
                        self.window_surface.blit(self.dropper_pic, [x, y])
                    if sprite == 'S':
                        self.window_surface.blit(self.syringe_pic, [x, y])                         
                    column_nbr += 1
                line_nbr += 1
            
            # Check player position
            self.player_position = self.player.player_position
            # display player
            self.window_surface.blit(self.player_pic, self.player_position)           
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit() 

                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.restart_rect.collidepoint(event.pos):
                            self.run = ""
                           
                        if self.quit_game_rect.collidepoint(event.pos):
                            quit()   
                
                #request movement using method movement_request() from Class Player()
                elif event.type == KEYDOWN:   
                    if event.key == K_RIGHT:
                        self.player.movement_request("RIGHT")        
                    if event.key == K_LEFT:
                        self.player.movement_request("LEFT")
                    if event.key == K_DOWN:
                        self.player.movement_request("DOWN")
                    if event.key == K_UP:
                        self.player.movement_request("UP")
                       
            # Refresh pygame display
            pygame.display.flip()

