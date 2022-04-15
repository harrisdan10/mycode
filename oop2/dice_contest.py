#!/usr/bin/python3
"""RZFeeser | Alta3 Research
   Running a simulation with our classes"""

# import our classes
from cheatdice import *

def main():
    """called at runtime"""

    # # the player known as the swapper
    swapper = Cheat_Swapper()
    # # the player known as the loaded_dice
    loaded_dice = Cheat_Loaded_Dice()

    dice_theif = Dice_Theif()

    # track scores for both players
    swapper_score = 0
    loaded_dice_score = 0
    dice_theif_score = 0

    # # how many games we want to run
    number_of_games = 100000
    game_number = 0

    # begin!
    print("Simulation running")
    print("==================")
    while game_number < number_of_games:
        swapper.roll()
        loaded_dice.roll()
        dice_theif.roll()

        swapper.cheat()
        loaded_dice.cheat()
        dice_theif.cheat()
        """Remove # before print statements to see simulation running
           Simulation takes approximately one hour to run with print
           statements or ten seconds with print statements
           commented out"""

        #print("Cheater 1 rolled" + str(swapper.get_dice()))
        #print("Cheater 2 rolled" + str(loaded_dice.get_dice()))
        if sum(swapper.get_dice()) == sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) == sum(dice_theif.get_dice()):
            #print("Draw!")
            pass
        elif sum(swapper.get_dice()) > sum(loaded_dice.get_dice()) and sum(swapper.get_dice()) > sum(dice_theif.get_dice()):
            #print("Dice swapper wins!")
            swapper_score+= 1
        elif sum(loaded_dice.get_dice()) > sum(swapper.get_dice()) and sum(loaded_dice.get_dice()) > sum(dice_theif.get_dice()):
            loaded_dice_score += 1
        else:
            #print("Loaded dice wins!")
            dice_theif_score += 1
        game_number += 1

    # the game has ended
    print("Simulation complete")
    print("-------------------")
    print("Final scores")
    print("------------")
    print(f"Swapper won: {swapper_score}")
    print(f"Loaded dice won: {loaded_dice_score}")
    print(f"Dice theif won: {dice_theif_score}")

    # determine the winner
    if swapper_score == loaded_dice_score:
        print("Game was drawn")
    elif swapper_score > loaded_dice_score:
        print("Swapper won most games")
    else:
        print("Loaded dice won most games")
    
    print(dice_theif.get_dice())
if __name__ == "__main__":
    main()
