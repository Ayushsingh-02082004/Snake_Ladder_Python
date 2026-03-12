from random import choice
from player import Player
from dice import Dice

def main():

    print("-----Welcome to the Snake and Ladder Game------")

    #uc1
    player1 = Player()

    options = ("NoPlay" , "Ladder" , "Snake")
    WINNING_POSITION = 100
    roll_count = 0

    #uc4 Repeat until the player reachess the winning position 
    while player1.position < WINNING_POSITION:
        roll_count += 1

        #Uc2 roll the die
        roll = Dice.roll()

        action = choice(options)

        match action :
            case "NoPlay":
                pass
            case "Ladder" :
                player1.position += roll
            case "Snake":
                player1.position = max(0 , player1.position-roll)

    print(f"Roll {roll_count} : Die({roll}) | Action: {action:7} | Position : {player1.position}")

    print("-" * 40)
    print(f"WINNER! You reached {player1.position} in {roll_count} rolls.")

if __name__ == "__main__":    
    main()

