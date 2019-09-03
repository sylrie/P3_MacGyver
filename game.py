""" game
    Manage active interface  
"""
import pygame
# programs import
from home_display import HomeDisplay
from laby_display import LabyDisplay
from win_display import WinDisplay
from lost_display import LostDisplay

class Game():

    def __init__(self):

        self.interface = "home"
        
        self.quit = False

        self.load_musics()
        self.display_interface()

    def load_musics(self):
        """ load musics
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
        """ Display the game
        """

        while not self.quit:

            if self.interface == "home":
  
                # play music
                self.home_music.play(3, 0 , 500) # play home music

                # display home
                self.home_interface = HomeDisplay()
                self.interface = self.home_interface.interface
                level = self.home_interface.level

                # stop music
                self.home_music.fadeout(500)  
            
            elif self.interface == "laby": 

                self.laby_sound.play(3, 0 , 500)

                self.laby_interface = LabyDisplay(level)
                self.interface = self.laby_interface.interface

                self.laby_sound.fadeout(500)

            elif self.interface == "win":

                self.win_music.play(3, 0 , 3000)

                self.win_interface = WinDisplay()
                self.interface = self.win_interface.interface

                self.win_music.fadeout(500)
            
            elif self.interface == "lost":

                self.lost_music.play(3, 0 , 3000)

                self.win_interface = LostDisplay()
                self.interface = self.win_interface.interface

                self.lost_music.fadeout(500)
        


    
