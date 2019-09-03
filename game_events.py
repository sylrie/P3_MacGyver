""" game events
    Manage game events 
"""
# library imports
import pygame

class Events():
    """ Manage events with sprite content and player position """

    def __init__(self, player):

        self.player = player
        
        self.loads()

    def loads(self):
        """ load resources
        """

        pygame.mixer.init()
        self.picked_sound = pygame.mixer.Sound("resources/sounds/picked.wav")  
        self.picked_sound.set_volume(0.2)
        self.lost_life = pygame.mixer.Sound("resources/sounds/lost_life.wav")
        self.lost_life.set_volume(0.3)
        self.win_sound = pygame.mixer.Sound("resources/sounds/win.wav")
        self.win_sound.set_volume(0.2)
        self.lost_sound = pygame.mixer.Sound("resources/sounds/lost.wav")
        self.lost_sound.set_volume(0.2)
        
    def actions(self):
        """ make actions with sprite content and player position """
               
        if self.player.sprite == "e":# water
            self.lost_life.play()
            self.player.health -=1   
            if self.player.health < 0:
                self.lost_sound.play()
                self.player.run = "lost"
                 
        elif self.player.sprite == "a":# Arrival
            if len(self.player.inventory) == 3:
                self.win_sound.play()
                self.player.run = "win"
            else:
                self.lost_sound.play()
                self.player.run = "lost"
        
        elif self.player.sprite == "H": # Health
            self.picked_sound.play()
            if self.player.health < 2:
                self.player.health += 1

        elif self.player.sprite == "p":
            pass

        else:
            self.player.inventory.append(self.player.sprite)
            self.picked_sound.play()
        
       
