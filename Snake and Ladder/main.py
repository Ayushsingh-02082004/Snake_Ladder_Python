from random import choice
from player import Player
from dice import Dice

def main():

    #uc1
    player1 = Player()

    options = ("NoPlay" , "Ladder" , "Snake")

    #Uc2 roll the die
    roll = Dice.roll()

    #UC3: check for Option
    option = choice(options)
    print(f"Rolled: {roll} | option: {option}")

    match option:
        case "NoPlay":
            pass
        case "Ladder":
            player1.position += roll
        case "Snake":
            player1.position -= roll

            if(player1.position < 0):
                player1.position = 0

    print(f"Current Position: {player1.position}")


if __name__ == "__main__":    
    main()

