from random import choice
from player import Player
from dice import Dice

def main():

    print("-----Welcome to the Snake and Ladder Game------")

    #uc7

    players = [Player() , Player()]
    player_names = ["Player 1" , "Player 2"]

    options = ("NoPlay" , "Ladder" , "Snake")

    WINNING_POSSITION = 100
    roll_count = 0
    current_player_idx = 0
    game_won = False

    while not game_won:

        roll_count += 1
        current_player = players[current_player_idx]
        current_name = player_names[current_player_idx]

        roll = Dice.roll()
        action = choice(options)

        match action:
            case "NoPlay":
                pass
            case "Ladder" if current_player.position + roll <= WINNING_POSSITION:
                current_player.position += roll
                print(f"Roll {roll_count:3} | {current_name} | Die: {roll} | Action: {action:7} | Position: {current_player.position}")
            case "Ladder":
                pass
                print(f"Roll {roll_count:3} | {current_name} | Die: {roll} | Action: {action:7} | Position: {current_player.position}")
            case "Snake":
                current_player.position = max(0, current_player.position - roll)
                print(f"Roll {roll_count:3} | {current_name} | Die: {roll} | Action: {action:7} | Position: {current_player.position}")

        #check for winner
        if current_player.position == WINNING_POSSITION:
            print("-" * 45)
            print(f"Congratulations  {current_name} WON THE GAME in {roll_count} total rolls! ")
            game_won  = True
        else:
            #switch to the other player (0 becomes 1 , 1 becomes 0)
            current_player_idx = 1-current_player_idx




if __name__ == "__main__":    
    main()

