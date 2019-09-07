""" game
    Manage active interface
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

#lybrary import
import pygame

# programs import
from frontend.interfaces.home_display import HomeDisplay
from frontend.interfaces.laby_display import LabyDisplay
from frontend.interfaces.win_display import WinDisplay
from frontend.interfaces.lost_display import LostDisplay

class Game():
    """ Manage interface display
    """

    def __init__(self):

        self.interface = "home"
        self.active_interface = None
        self.quit = False

        self.load_musics()
        self.display_interface()

    def load_musics(self):
        """ load musics needed
        """

        pygame.mixer.init()

        self.home_music = pygame.mixer.Sound("resources/sounds/home_music.ogg")
        self.home_music.set_volume(0.4)

        self.laby_sound = pygame.mixer.Sound("resources/sounds/game_music.ogg")
        self.laby_sound.set_volume(0.4)

        self.win_music = pygame.mixer.Sound("resources/sounds/win_music.ogg")
        self.win_music.set_volume(0.4)

        self.lost_music = pygame.mixer.Sound("resources/sounds/lost_music.ogg")
        self.lost_music.set_volume(0.4)

    def display_interface(self):
        """ Display needed interface
        """

        while not self.quit:

            if self.interface == "home":

                self.home_music.play(3, 0, 500)

                self.active_interface = HomeDisplay()
                self.interface = self.active_interface.interface

                self.home_music.fadeout(500)

            elif self.interface == "laby":

                self.laby_sound.play(3, 0, 500)

                self.active_interface = LabyDisplay()
                self.interface = self.active_interface.interface

                self.laby_sound.fadeout(500)

            elif self.interface == "win":

                self.win_music.play(3, 0, 3000)

                self.active_interface = WinDisplay()
                self.interface = self.active_interface.interface

                self.win_music.fadeout(500)

            elif self.interface == "lost":

                self.lost_music.play(3, 0, 3000)

                self.active_interface = LostDisplay()
                self.interface = self.active_interface.interface

                self.lost_music.fadeout(500)
