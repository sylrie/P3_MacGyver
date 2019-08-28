import pygame
from pygame import mixer

class Events():

    def __init__(self):
        
        self.load_sounds()

    def load_sounds(self):

        pygame.mixer.init()

        self.music_sound = pygame.mixer.Sound("resources/sounds/music.ogg")

        self.picked_sound = pygame.mixer.Sound("resources/sounds/picked.wav")
        
        self.lost_life = pygame.mixer.Sound("resources/sounds/lost_life.ogg")
        
        self.win_sound = pygame.mixer.Sound("resources/sounds/win.wav")

    def actions(self, sprite, inventory, health, run):
     
        self.sprite_content= sprite
        self.inventory = inventory
        self.health = health
        self.run = run
       
        if self.sprite_content == "T":
            self.inventory.append("tube")
            self.picked_sound.play()
        
        if self.sprite_content == "S":
            self.inventory.append("syringe")
            self.picked_sound.play()

        if self.sprite_content == "D":
            self.inventory.append("dropper")
            self.picked_sound.play()
        
        if self.sprite_content == "H": # Health
            self.picked_sound.play()
            if self.health < 2:
                self.health += 1

        if self.sprite_content == "F":# Fire
            self.lost_life.play()
            self.health -=1
            if self.health < 0:
                self.run = "lost"
                 
        if self.sprite_content == "a":# Arrival
            if len(self.inventory) == 3:
                self.win_sound.play()
                self.run = "win"
            else:
                self.run = "lost"

        
