from player import Player
from dice import Dice

def play_uc2():

    #UC1 initialize player
    user = Player()
    print(f"Game Started. Player position: {user.position}")

    #UC2 :Roll the die 

    roll_value = Dice.roll()
    print(f"Die Rolled: {roll_value}")


    user.position += roll_value
    print(f"Player moved to: {user.positon}")


    if __name__ == "__main__":
        play_uc2()