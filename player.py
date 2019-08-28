
import items
from game_events import *


class Player():

    def __init__(self):
        
        self.sprite_cote = 30
          
        self.line_pos = None
        self.column_pos = None
        self.player_position = ()

        # From Class Items()
        self.laby = items.Items()
        self.labyrinth = self.laby.labyrinth

        # From Class Events()
        self.actions = Events()
        
        self.inventory = []
        self.health = 2
        self.run = "game"

        self.get_init_position()

    # Find initial player position 'd'
    def get_init_position (self):
        
        self.line_pos = 0
        self.column_pos = 0
        position = "d"
        count_line = 0
        search = 1
        while search == 1:
            
            for line in self.labyrinth:

                if position in line:
                    self.line_pos = count_line
                    column_pos = self.labyrinth[self.line_pos].index(position)
                    search = 0
                    self.player_position = (self.line_pos, self.column_pos)
                    
                count_line += 1  

    # movement request from directional keys
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
        
        # next sprite
        self.sprite_content = self.labyrinth[line_pos][column_pos]

        # run 'move' method
        self.move(self.sprite_content, line_pos, column_pos)
    
    # check the next sprite before change player position and run method 'actions' from Class Events
    def move(self, sprite, line_pos, column_pos):
     
        self.sprite = sprite
       
        # check the new srite
        if self.sprite == "w": # if it's a wall, cancel movement
            line_pos = self.line_pos 
            column_pos = self.column_pos
        
        if self.sprite_content != "w": # if it's not a wall, make actions
            
            # run method 'action' of class Events
            self.actions.actions(self.sprite_content, self.inventory, self.health, self.run)
            self.health = self.actions.health
            self.run = self.actions.run
        
            # modify sprite content of actual position
            if self.labyrinth[self.line_pos][self.column_pos] != "F":
                self.labyrinth[self.line_pos][self.column_pos] = "p"
            
            #change the player position
            self.line_pos = line_pos
            self.column_pos = column_pos
            self.player_position = [self.column_pos*self.sprite_cote, self.line_pos*self.sprite_cote]

        
