import pygame
from pygame.locals import *
import game_events

class Home():

    def __init__(self):

        self.run = "home"
        self.display_infos = 0
        
        self.create_surface()
        self.loads_home()
        self.create_rect()
        self.display()

    def create_surface(self):

        pygame.init()
        pygame.display.set_caption("MacGyver Labyrinth")
        self.window_surface = pygame.display.set_mode((450, 520))

    def loads_home(self):
        # Loading images
        self.home_pic = pygame.image.load("resources/images/home.jpg").convert()
        self.info_button = pygame.image.load("resources/images/i.png").convert()
        self.start_button = pygame.image.load("resources/images/start.png").convert()
        self.quit_button = pygame.image.load("resources/images/quit.png").convert()
        self.info_pic = pygame.image.load("resources/images/info.png").convert()

        #loading sounds
        

    def create_rect(self):

        self.start_rect = pygame.Rect((293, 62), (130, 126))
        self.quit_rect = pygame.Rect((28, 62), (130, 126))
        self.info_rect = pygame.Rect((210, 65), (30, 24))

    def display(self):

        while self.run == "home":

            pygame.time.Clock().tick(30)
            

            self.window_surface.blit(self.home_pic, [0,0])
            self.window_surface.blit(self.info_button, [210, 65])
            self.window_surface.blit(self.start_button, [293, 62])
            self.window_surface.blit(self.quit_button, [28, 62])
                
            if self.display_infos == 1:
                self.window_surface.blit(self.info_pic, [35,340])


            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                    
                        if self.quit_rect.collidepoint(event.pos):
                            quit()

                        if self.start_rect.collidepoint(event.pos): # run the game display
                            self.run = 0
                            

                        if self.info_rect.collidepoint(event.pos): # active show infos
                            self.display_infos = 1 

                elif event.type == MOUSEBUTTONUP:
                    if event.button == 1:
                        #if self.info_rect.collidepoint(event.pos):# close show infos
                        self.display_infos = 0


            pygame.display.flip()
