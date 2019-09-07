""" player
    manage player
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# programs import
from backend.game_events import Events

class Player():
    """ Create a player and manage palyer attribut
    """

    def __init__(self, labyrinth):

        self.labyrinth = labyrinth

        self.line_pos = None
        self.column_pos = None
        self.player_position = ()

        # From Class Events()
        self.actions = Events(self)

        self.inventory = []
        self.health = 2
        self.run = "game"

        self.get_init_position()

    def get_init_position(self):
        """ Find initial player position 'd'
        """

        self.line_pos = 0
        self.column_pos = 0
        position = "d"
        count_line = 0
        search = 1
        while search == 1:

            for line in self.labyrinth:

                if position in line:
                    self.line_pos = count_line
                    self.column_pos = self.labyrinth[self.line_pos].index(position)
                    search = 0
                    self.player_position = (self.column_pos, self.line_pos)

                count_line += 1

    def movement_request(self, movement):
        """ Movement request from directional keys
        """

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
                line_pos += 1

        elif self.movement == "UP":
            if line_pos > 0:
                line_pos -= 1

        # run 'move' method
        self.move(line_pos, column_pos)

    def move(self, line_pos, column_pos):
        """ check the next sprite before change player position
        run method 'actions' from Class Events
        """

        self.sprite = self.labyrinth[line_pos][column_pos]

        # if sprite is not a wall
        if self.sprite != "w":

            # run method 'action' of class Events
            self.actions.actions()

            if self.sprite == "f" and not "S" in self.inventory:

                self.get_init_position()
                
                
            # modify sprite content of actual position
            else:
                self.labyrinth[line_pos][column_pos] = "p"

                #change the player position
                self.line_pos = line_pos
                self.column_pos = column_pos
                self.player_position = [self.column_pos, self.line_pos]
