import pygame
from pygame.locals import *
from constant import *
from labyrinth import *
#from game_display import *


class Event_game():
    """
    """

    def __init__(self):
        
        
        labyrinth = Create_game()
        self.labyrinth = labyrinth.labyrinth.labyrinth

        

        self.line_pos = 0
        self.column_pos = 0
        self.player_pos = [0, 0]
        

    def movement_request(self, movement):

        
        self.movement = movement
        line_pos = self.line_pos 
        column_pos = self.column_pos

        

        if self.movement == "RIGHT":
            if column_pos < 15:
                column_pos += 1
            
        elif self.movement == "LEFT":
            if column_pos > 0:
                column_pos -= 1

        elif self.movement == "DOWN":
            if line_pos < 15:
                line_pos +=1

        elif self.movement == "UP":
            if line_pos > 0:
                line_pos -= 1
                

        sprite_content = self.labyrinth[line_pos][column_pos]
        if sprite_content != "w":
            self.labyrinth[self.line_pos][self.column_pos] = "p"
            self.line_pos = line_pos
            self.column_pos = column_pos
            self.player_pos = [self.column_pos * sprite_cote, self.line_pos * sprite_cote]

        else :
            line_pos = self.line_pos 
            column_pos = self.column_pos
            
                   


            




        
