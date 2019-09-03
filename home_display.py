""" home display
    display home interface
"""
# library imports
import pygame

# programs import


class HomeDisplay():
    """ Display home interface
    """

    def __init__(self):

        self.interface = "home"
        self.level = "level1"
        self.display_infos = False
        
        self.create_surface()
        self.loads()
        self.create_rect()
        self.display()

    def create_surface(self):
        """ Create pygame surface
        """

        pygame.init()
        pygame.display.set_caption("MacGyver Labyrinth")
        self.window_surface = pygame.display.set_mode((450, 520), pygame.NOFRAME)

    def loads(self):
        """ load resources
        """
        
        # Loading images
        self.home_pic = pygame.image.load("resources/images/home.png").convert()
        self.info_button = pygame.image.load("resources/images/B_infos.png").convert_alpha()
        self.start_button = pygame.image.load("resources/images/B_start.png").convert()
        self.quit_button = pygame.image.load("resources/images/B_quitter.png").convert()
        self.info_pic = pygame.image.load("resources/images/infos.png").convert_alpha()
        
        self.level1_on = pygame.image.load("resources/images/lvl1_on.png").convert()
        self.level1_off = pygame.image.load("resources/images/lvl1_off.png").convert()
        
        self.level2_on = pygame.image.load("resources/images/lvl2_on.png").convert()
        self.level2_off = pygame.image.load("resources/images/lvl2_off.png").convert()

    def create_rect(self):
        """ Create rect surfaces
        """

        self.start_rect = pygame.Rect((345, 15), (100, 30))
        self.quit_rect = pygame.Rect((5, 15), (100, 30))
        self.info_rect = pygame.Rect((200, 15), (50, 30))
        self.level1_rect = pygame.Rect((95, 475), (100, 30))
        self.level2_rect = pygame.Rect((255, 475), (100, 30))

    def display(self):
        """ Display home iterface
        """
        
        loop = True
        while loop:
        
            self.window_surface.blit(self.home_pic, [0,45])
            self.window_surface.blit(self.info_button, [200, 15])
            self.window_surface.blit(self.start_button, [345, 15])
            self.window_surface.blit(self.quit_button, [5, 15])
            
            # level
            if self.level == "level1":
                self.window_surface.blit(self.level1_on, [95, 475])
                self.window_surface.blit(self.level2_off, [255, 475])
            elif self.level == "level2":
                self.window_surface.blit(self.level1_off, [95, 475])
                self.window_surface.blit(self.level2_on, [255, 475])
                
            if self.display_infos == 1:
                self.window_surface.blit(self.info_pic, [35,200])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                    
                        if self.quit_rect.collidepoint(event.pos):
                            quit()

                        elif self.start_rect.collidepoint(event.pos): # run the game display
                            self.interface = "laby"
                            loop = False
                            
                        elif self.info_rect.collidepoint(event.pos): # active show infos
                            self.display_infos = True

                        elif self.level1_rect.collidepoint(event.pos):
                            self.level = "level1"
                        elif self.level2_rect.collidepoint(event.pos):
                            self.level = "level2"

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        #if self.info_rect.collidepoint(event.pos):# close show infos
                        self.display_infos = 0


            pygame.display.flip()


