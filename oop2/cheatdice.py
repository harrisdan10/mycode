#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Creating a simple dice program utilizing classes."""

# standard library
from random import randint

class Player:
    def __init__(self):
        self.dice = []

    def roll(self):
        self.dice = [] # clears current dice
        for i in range(3):  # make 3 rolls
            self.dice.append(randint(1,6))   # 1 to 6 inclusive

    def get_dice(self): # returns the dice rolls
        return self.dice

# # allows user to turn their last roll into a 6
class Cheat_Swapper(Player):  # inheritance of Player
    def cheat(self):
        self.dice[-1] = 6

# allows user to increase all rolls if they were less than a 6
class Cheat_Loaded_Dice(Player): # inheritance of Player
  def cheat(self):
      i = 0
      while i < len(self.dice):
          if self.dice[i] < 6:
              self.dice[i] += 1
          i += 1


loaded = Cheat_Loaded_Dice()
swapper = Cheat_Swapper()

class Dice_Theif(Player):
    def cheat(self):
        i = 0
        copy1 = ''
        copy2 = ''
        while i < len(self.dice):
            if self.dice[i] < 4:

                loaded.roll()
                loaded.cheat()

                swapper.roll()
                swapper.cheat()

                for roll in loaded.get_dice():
                    if roll > 4:
                        copy1 = roll
        
                for roll in swapper.get_dice():
                    if roll > 4:
                        copy2 = roll

                if copy1 > copy2:
                    self.dice[i] = copy1
                elif copy1 == copy2:
                    self.dice[i] = copy1
                else: 
                    self.dice[i] = copy2
            i += 1
