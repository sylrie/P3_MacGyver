""" game
    Manage active interface
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

#lybrary import
from pygame import mixer

# programs import

from frontend.interfaces.maze_display import MazeDisplay
from frontend.interfaces.secondary_display import SecondaryDisplay

class Game():
    """ Manage interface display
    """

    def __init__(self):

        self.interface = "home"
        self.active_interface = None
        self.music = ""
        self.quit = False

        self.display_interface()

    def load_music(self):
        """ load musics needed
        """

        mixer.init()
        path = "resources/sounds/" + self.interface +"_music.ogg"

        self.music = mixer.Sound(path)
        self.music.set_volume(0.4)

    def display_interface(self):
        """ Display needed interface
        """

        while not self.quit:

            self.load_music()

            if self.interface == "maze":

                self.music.play(3, 0, 500)

                self.active_interface = MazeDisplay()
                self.interface = self.active_interface.interface

                self.music.fadeout(500)

            else:
                self.music.play(3, 0, 0)

                self.active_interface = SecondaryDisplay(self.interface)
                self.interface = self.active_interface.active_interface

                self.music.fadeout(500)
