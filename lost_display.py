""" lost display
    display end interface
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# pylint: disable=no-member

# library import
import pygame

class LostDisplay():
    """  Display lost interface
    """

    def __init__(self):

        self.interface = ""

        self.create_surface()
        self.loads()
        self.create_rect()
        self.display()

    def create_surface(self):
        """ create pygame surface
        """

        pygame.display.init()
        self.window_surface = pygame.display.set_mode((450, 520), pygame.NOFRAME)

    def loads(self):
        """ load resources
        """

        # Loading images
        self.lost_pic = pygame.image.load("resources/images/lost.png").convert()
        self.restart_button = pygame.image.load("resources/images/B_restart.png").convert()
        self.home_button = pygame.image.load("resources/images/B_home.png").convert()

    def create_rect(self):
        """ Create rect surfaces
        """

        self.restart_rect = pygame.Rect((170, 400), (180, 25))
        self.home_rect = pygame.Rect((170, 450), (180, 25))

    def display(self):
        """ Display lost iterface
        """

        loop = True
        while loop:

            pygame.time.Clock().tick(30)
            #self.win_sound.play()
            self.window_surface.fill((0, 0, 0))
            self.window_surface.blit(self.restart_button, [170, 400])
            self.window_surface.blit(self.home_button, [170, 450])
            self.window_surface.blit(self.lost_pic, [0, 0])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.home_rect.collidepoint(event.pos):
                            self.interface = "home"
                            loop = False
                        if self.restart_rect.collidepoint(event.pos):
                            self.interface = "laby"
                            loop = False

            pygame.display.flip()
