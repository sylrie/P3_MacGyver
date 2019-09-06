""" game events
    Manage game events
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# library import
from pygame import mixer

class Events():
    """ Manage events with sprite content and player position """

    def __init__(self, player):

        self.player = player

        self.loads()

    def loads(self):
        """ load sounds
        """

        mixer.init()
        self.picked_sound = mixer.Sound("resources/sounds/picked.wav")
        self.picked_sound.set_volume(0.2)
        self.lost_life = mixer.Sound("resources/sounds/lost_life.wav")
        self.lost_life.set_volume(0.3)
        self.win_sound = mixer.Sound("resources/sounds/win.wav")
        self.win_sound.set_volume(0.2)
        self.lost_sound = mixer.Sound("resources/sounds/lost.wav")
        self.lost_sound.set_volume(0.2)

    def actions(self):
        """ make actions with sprite content and player position """

        if self.player.sprite == "e":# water
            self.lost_life.play()
            self.player.health -= 1
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

        elif self.player.sprite == "L": # Health
            self.picked_sound.play()
            if self.player.health < 2:
                self.player.health += 1

        elif self.player.sprite != "p" and self.player.sprite != "d":
            self.player.inventory.append(self.player.sprite)
            self.picked_sound.play()
