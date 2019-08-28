#import pygame
#from pygame.locals import *

import player
import home_display 
import game_display
import end_display
import pprint

        


class Display_interface():
    
    def __init__(self):

        self.home = home_display
        self.game = game_display
        self.end = end_display

        self.run = "home"
        
        self.display()
        
    def display(self):  

        display = 1
        while display == 1:

            while self.run == "home":

                self.home.Home()
                self.run = "game"

            while self.run == "game":

                self.game.Game()
                self.run = "end"

            while self.run == "end":
                
                self.run_end = player.Player()
                self.run_end = self.run_end.run
                print(self.run_end)
                self.end.End(self.run_end)

                self.run = "end"
                    
            display = 0
                    
    
p = Display_interface()
p
    
     

          

