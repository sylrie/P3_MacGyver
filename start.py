import pygame
from pygame import mixer

import home_display 
import game_display
import end_display
import player

class Display_interface():
    
    def __init__(self):

        self.home = home_display
        self.game = game_display
        self.end = end_display
        
        self.event = player.Player()

        self.load_sounds()
        self.display()
    
    def load_sounds(self):
        pygame.mixer.init()
        self.music_sound = pygame.mixer.Sound("resources/sounds/music.ogg")
        self.music_sound.set_volume(0.1)

    def display(self):  

        self.run = self.event.run
        display = 1
        while display == 1:

            
            self.music_sound.play(3, 0, 2000)
            self.home.Home()
   
            self.game.Game()
            
            print(self.run)    
        
      
            self.end.End(self.run)           
                

            
                
               
                
                    
        display = 0
                    
    
p = Display_interface()
p
    
     

          

