""" player
    manage player
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# programs import
from backend.game_events import GameEvents

class Player():
    """ Create a player and manage palyer attribut
    """

    def __init__(self, maze):

        self.maze = maze

        self.line_pos = None
        self.column_pos = None
        self.player_position = ()
        self.movement = ""
        self.sprite = ()

        # From Class Events()
        self.actions = GameEvents(self)

        self.inventory = []
        self.health = 2
        self.game_status = "game"

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

            for line in self.maze:

                if position in line:
                    self.line_pos = count_line
                    self.column_pos = self.maze[self.line_pos].index(position)
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
        if self.movement == "RIGHT" and column_pos < 14:          
            column_pos += 1

        elif self.movement == "LEFT" and column_pos > 0:
            column_pos -= 1

        elif self.movement == "DOWN" and line_pos < 14:
            line_pos += 1

        elif self.movement == "UP" and line_pos > 0:
            line_pos -= 1

        # call 'move' method
        self.move(line_pos, column_pos)

    def move(self, line_pos, column_pos):
        """ check the next sprite before change player position
            use method 'actions' from Class Events
        """
        # new sprite content
        self.sprite = self.maze[line_pos][column_pos]

        # if sprite is not a wall
        if self.sprite != "w":

            # call 'action'method of class Events
            self.actions.actions()

            # if Golem without Sword
            if self.sprite == "f" and "S" not in self.inventory:
                self.get_init_position()

            else:
                # modify sprite content of new position
                self.maze[line_pos][column_pos] = "p"

                #change the player position
                self.line_pos = line_pos
                self.column_pos = column_pos
                self.player_position = [self.column_pos, self.line_pos]
