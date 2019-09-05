""" end display
    display end interface
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# pylint: disable=no-member

# library import
import pygame

class WinDisplay():
    """  Display end interface
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
        self.window_surface = pygame.display.set_mode((450, 520), pygame.noframe)

    def loads(self):
        """ load resources
        """

        # Loading images
        self.win_pic = pygame.image.load("resources/images/win.png").convert()
        self.quit_button = pygame.image.load("resources/images/B_quitter.png").convert()
        self.home_button = pygame.image.load("resources/images/B_home.png").convert()

    def create_rect(self):
        """ Create rect surfaces
        """

        self.quit_rect = pygame.Rect((170, 400), (180, 25))
        self.home_rect = pygame.Rect((170, 450), (180, 25))

    def display(self):
        """ Display home iterface
        """

        loop = 1
        while loop == 1:

            pygame.time.Clock().tick(30)
            #self.win_sound.play()
            self.window_surface.fill((0, 0, 0))
            self.window_surface.blit(self.quit_button, [170, 400])
            self.window_surface.blit(self.home_button, [170, 450])
            self.window_surface.blit(self.win_pic, [0, 20])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.home_rect.collidepoint(event.pos):
                            self.interface = "home"
                            loop = False
                        if self.quit_rect.collidepoint(event.pos):
                            quit()

            pygame.display.flip()
