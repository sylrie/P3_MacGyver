""" game events
    Manage game events
"""

#!/usr/bin/python3
# -*- coding: Utf-8 -*

# library import
import time
from pygame import mixer

class GameEvents():
    """ Manage events with sprite content and player position """

    def __init__(self, player):

        self.player = player

        self.load_sounds()

    def load_sounds(self):
        """ load sounds and set volume
        """

        # init module mixer
        mixer.init()

        self.picked_sound = mixer.Sound("resources/sounds/picked.wav")
        self.picked_sound.set_volume(0.2)

        self.lost_life = mixer.Sound("resources/sounds/lost_life.wav")
        self.lost_life.set_volume(0.4)

        self.kill_golem = mixer.Sound("resources/sounds/kill_golem.wav")
        self.kill_golem.set_volume(0.7)

        self.sword_sound = mixer.Sound("resources/sounds/sword.wav")

    def actions(self):
        """ make actions with sprite content and player position """

        if self.player.sprite == "f": # Golem
            self.sword_sound.play(1)
            time.sleep(1)

            # if sword not in inventory
            if not "S" in self.player.inventory:
                self.lost_life.play()
                self.player.health -= 1
                # if no life remaining
                if self.player.health < 0:
                    self.player.game_status = "lost"

            # if sword in inventory
            else:
                self.kill_golem.play()

        elif self.player.sprite == "a":# Arrival
            self.sword_sound.play(1)
            time.sleep(1)

            # if all items picked
            if len(self.player.inventory) == 3:
                self.player.game_status = "win"
            else:
                self.player.game_status = "lost"

        elif self.player.sprite == "L": # Life
            self.picked_sound.play()
            # if life not full, add life
            if self.player.health < 2:
                self.player.health += 1

        elif self.player.sprite in ("A", "H", "S"): #Items
            # Add item to inventory
            self.player.inventory.append(self.player.sprite)
            self.picked_sound.play()
