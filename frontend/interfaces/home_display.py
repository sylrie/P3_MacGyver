""" home display
    display home interface
"""
#!/usr/bin/python3
# -*- coding: Utf-8 -*

# pylint: disable=no-member

# library import
import pygame

class HomeDisplay():
    """ Display home interface
    """

    def __init__(self):

        self.interface = "home"
        self.display_infos = False
        self.loop = True

        self.create_surface()
        self.loads()
        self.create_rect()
        self.display()

    def create_surface(self):
        """ Create pygame surface
        """

        pygame.display.init()
        self.window_surface = pygame.display.set_mode((450, 520), pygame.NOFRAME)

    def loads(self):
        """ load resources
        """

        self.home_pic = pygame.image.load("resources/images/home.png").convert()

        self.info_button = pygame.image.load("resources/images/B_infos.png").convert_alpha()
        self.info_pic = pygame.image.load("resources/images/infos.png").convert_alpha()

        self.start_button = pygame.image.load("resources/images/B_start.png").convert()
        self.quit_button = pygame.image.load("resources/images/B_quitter.png").convert()

    def create_rect(self):
        """ Create rect surfaces
        """

        self.start_rect = pygame.Rect((345, 15), (100, 30))
        self.quit_rect = pygame.Rect((5, 15), (100, 30))
        self.info_rect = pygame.Rect((200, 15), (50, 30))

    def pygame_event(self):
        """ manage pygame event
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if self.quit_rect.collidepoint(event.pos):
                        quit()

                    elif self.start_rect.collidepoint(event.pos): # run the game display
                        self.interface = "laby"
                        self.loop = False

                    elif self.info_rect.collidepoint(event.pos): # active show infos
                        if self.display_infos:
                            self.display_infos = False
                        else:
                            self.display_infos = True

    def display(self):
        """ Display home iterface
        """

        self.loop = True
        while self.loop:

            self.window_surface.blit(self.home_pic, [0, 45])
            self.window_surface.blit(self.info_button, [200, 15])
            self.window_surface.blit(self.start_button, [345, 15])
            self.window_surface.blit(self.quit_button, [5, 15])

            if self.display_infos:
                self.window_surface.blit(self.info_pic, [35, 80])

            self.pygame_event()

            pygame.display.flip()
