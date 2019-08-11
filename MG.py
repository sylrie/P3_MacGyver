#! /usr/bin/env python3
# conding: utf-8

import pprint
from random import randrange, choice

class Labyrinth():
    """
    Create labyrinth 
    """

    def __init__(self):

        self.txt_labyrinth = ""
        self.manipulable_labyrinth = []
        self.get_txt_labytinth()
        self.get_manipulable_labyrinth()

    def get_txt_labytinth(self): 
        with open ("N1.txt", "r") as labyritnh_file:
            self.txt_labyrinth = labyritnh_file.read()

    def get_manipulable_labyrinth(self):
        split_laby = self.txt_labyrinth.split("\n")
        for line in split_laby:
            laby_line = []
            for caracter in line:
                laby_line.append(caracter)
            self.manipulable_labyrinth.append(laby_line)

class Item():
    """
    Add items at random position
    Using random (randrange and choice)
    """

    def __init__(self, labyrinth):
        self.labyrinth = labyrinth
        self.create_ether()
        self.create_needle()
        self.create_syringe()

    def random_position(self):
        lines = len(self.labyrinth) - 1
        random_line = randrange(lines)
        line = self.labyrinth[random_line]
        columns = []
        count = 0
        for caracter in line:
            if caracter == "p":
                columns.append(count)
            count += 1
        random_column = choice(columns)    

        return (random_line, random_column)

    def create_needle(self):
        pos = self.random_position()
        self.labyrinth[pos[0]][pos[1]] = "N"
    
    def create_ether(self):
        pos = self.random_position()
        self.labyrinth[pos[0]][pos[1]] = "E"

    def create_syringe(self):
        pos = self.random_position()
        self.labyrinth[pos[0]][pos[1]] = "S"

class Game():
    def __init__(self):
        self.labyrinth = Labyrinth()
        self.item = Item(labyrinth=self.labyrinth.manipulable_labyrinth)

class Characters():

game = Game()
pprint.pprint(game.labyrinth.manipulable_labyrinth)
