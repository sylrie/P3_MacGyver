import pygame
from pygame.locals import *
from constant import *
from labyrinth import *


class Event_game():
    """
    """

    def __init__(self):
                
        labyrinth = Create_game()
        self.labyrinth = labyrinth.labyrinth.labyrinth

        init_position = Game()
        self.line_pos = init_position.line_pos
        self.column_pos = init_position.column_pos
        self.player_pos = [self.column_pos, self.line_pos]

        self.end_game = ""
        self.health = 2
        self.items = ["tube", "syringe", "dropper"]
        self.picked_item = 0
        self.lost_life = 0
            

    def movement_request(self, movement):
        
        self.movement = movement
        line_pos = self.line_pos 
        column_pos = self.column_pos

        #calculate the next sprite with the movement request
        if self.movement == "RIGHT":
            if column_pos < 14:
                column_pos += 1
            
        elif self.movement == "LEFT":
            if column_pos > 0:
                column_pos -= 1

        elif self.movement == "DOWN":
            if line_pos < 14:
                line_pos +=1

        elif self.movement == "UP":
            if line_pos > 0:
                line_pos -= 1

                
        # Manage events with sprite content
        sprite_content = self.labyrinth[line_pos][column_pos]

        # if wall, cancel movement request
        if sprite_content == "w":
            line_pos = self.line_pos 
            column_pos = self.column_pos


        if sprite_content == "F":
            self.health -= 1
            self.lost_life = 1
            line_pos = 0 
            column_pos = 0
            self.line_pos = line_pos
            self.column_pos = column_pos
            self.player_pos = [0, 0]
            
        # if not a wall
        if sprite_content != "w":
            self.picked_item = 0
            self.lost_life = 0
            
            if sprite_content == "T":
                self.items.remove("tube")
                self.picked_item = 1

            if sprite_content == "S":
                self.items.remove("syringe")
                self.picked_item = 1

            if sprite_content == "D":
                self.items.remove("dropper")
                self.picked_item = 1

            if sprite_content == "H":
                self.picked_item = 1
                if self.health < 2:
                    self.health += 1
            
  
                    
        # end of game
            if sprite_content == "a":
                if len(self.items) == 0:
                    self.end_game = "win"
                else:
                    self.end_game = "lost"
            
            if self.health <= -1:
                self.end_game = "lost"

        #change the player position
        self.labyrinth[self.line_pos][self.column_pos] = "p"
        self.line_pos = line_pos
        self.column_pos = column_pos
        self.player_pos = [self.column_pos * sprite_cote, self.line_pos * sprite_cote]
    

        
            
                   


            




        
