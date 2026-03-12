def start_game():
    # UC1: Initialize the player at position 0
    player_position = 0
    
    print("--- Welcome to Snake and Ladder Game ---")
    print(f"Game Started. Player is at position: {player_position}")
    
    return player_position

if __name__ == "__main__":
    current_pos = start_game()