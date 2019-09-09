""" Secondary display
    display interfaces for 'home', 'lost' and 'win'
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# pylint: disable=no-member

# library import
import pygame

class SecondaryDisplay():
    """  Display secondary interfaces
         Home - Win - Lost
    """

    def __init__(self, interface):

        self.active_interface = interface
        self.loop = True
        self.display_infos = False

        self.create_surface()
        self.load_images()
        self.create_rect()
        self.display()

    def create_surface(self):
        """ create pygame surface
        """

        pygame.display.init()

        icone = pygame.image.load("resources/images/icon.png")
        pygame.display.set_icon(icone)

        pygame.display.set_caption("MacGyver Labyrinth")
        self.window_surface = pygame.display.set_mode((450, 520))

    def load_images(self):
        """ load resources
        """

        if self.active_interface == "lost":
            self.interface_pic = pygame.image.load("resources/images/lost.png").convert()

        elif self.active_interface == "win":
            self.interface_pic = pygame.image.load("resources/images/win.png").convert()

        else:
            self.interface_pic = pygame.image.load("resources/images/home.png").convert()
            self.info_pic = pygame.image.load("resources/images/info.png").convert()

    def create_rect(self):
        """ Create rect surfaces
        """

        self.quit_rect = pygame.Rect((175, 450), (100, 30))

        if self.active_interface == "home":
            self.start_rect = pygame.Rect((175, 400), (100, 30))
            self.info_rect = pygame.Rect((200, 80), (50, 30))

        else:
            self.home_rect = pygame.Rect((175, 400), (100, 30))
            self.start_restart_rect = pygame.Rect((175, 350), (100, 30))

    def pygame_event_home(self):
        """ Manage Home pygame event"""

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if self.start_rect.collidepoint(event.pos):
                        self.active_interface = "laby"
                        self.loop = False

                    elif self.quit_rect.collidepoint(event.pos):
                        quit()

                    elif self.info_rect.collidepoint(event.pos):
                        if self.display_infos:
                            self.display_infos = False
                        else:
                            self.display_infos = True

    def pygame_event(self):
        """ Manage Win and Lost pygame event"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:

                    if self.home_rect.collidepoint(event.pos):
                        self.active_interface = "home"
                        self.loop = False

                    if self.start_restart_rect.collidepoint(event.pos):
                        self.active_interface = "laby"
                        self.loop = False

                    if self.quit_rect.collidepoint(event.pos):
                        quit()

    def display(self):
        """ Display lost iterface
        """

        #self.loop = True
        while self.loop:

            self.window_surface.fill((0, 0, 0))
            self.window_surface.blit(self.interface_pic, [0, 0])

            if self.display_infos:
                self.window_surface.blit(self.info_pic, [35, 130])

            if not self.active_interface == "home":
                self.pygame_event()
            else:
                self.pygame_event_home()

            pygame.display.flip()
