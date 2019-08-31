import pygame
from pygame.locals import *
import player



class End():

    def __init__(self, end):
        
        self.end = end
        self.event = player.Player()
        
        self.create_surface()
        self.loads()
        self.create_rect()
        self.display()

    def create_surface(self):

        pygame.init()
        pygame.display.set_caption("MacGyver Labyrinth")
        self.window_surface = pygame.display.set_mode((450, 520))

    def loads(self):
        # Loading images
        self.lost_pic = pygame.image.load("resources/images/lost.jpg").convert()
        self.win_pic = pygame.image.load("resources/images/win.jpg").convert()
        self.restart_button = pygame.image.load("resources/images/restart.png").convert()
        self.quit_button = pygame.image.load("resources/images/game_quit.png").convert()
        
        #loading sounds
        self.win_sound = pygame.mixer.Sound("resources/sounds/win.wav")
        self.win_sound.set_volume(0.1)

    def create_rect(self):

        self.restart_rect = pygame.Rect((5, 456), (180, 25))
        self.quit_rect = pygame.Rect((5, 490), (180, 25))
        
    def display(self):
        run_end = 1
        while run_end == 1:
            

            pygame.time.Clock().tick(30)
            #self.win_sound.play()
            self.window_surface.fill((0, 0, 0))
            self.window_surface.blit(self.restart_button, [5, 456])
            self.window_surface.blit(self.quit_button, [5, 490])
            if self.end == "win":
                self.window_surface.blit(self.win_pic, [0, 200])
            if self.end == "lost":
                self.window_surface.blit(self.lost_pic, [0, 0])

            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
                elif event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:                    
                        if self.quit_rect.collidepoint(event.pos):
                            quit()
                        if self.restart_rect.collidepoint(event.pos): 
                            self.run = "off"
                            

            pygame.display.flip()
