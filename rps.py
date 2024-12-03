from random import randint
import os

# Setting up constants that will be used later.
MOVES = ["rock", "paper", "scissors"]

GAME_OPTIONS = """
====================
0: Exit

1: One Match
2: Best of Three
3: Best of Ten
====================
"""

MOVE_OPTIONS = """
====================
Rock
Paper
Scissors
====================
"""

# Creating the main function that will be used to start Rock Paper Scissors games.
def rockPaperScissors():    
    print("Rock Paper Scissors! Choose:")
    print(MOVE_OPTIONS)

    user_input = input("-> ").lower()

    if not user_input in MOVES:
        print("Invalid Move")
        return
    
    plr_move = MOVES.index(user_input)
    bot_move = randint(0, 2)

    game_results = (3 + plr_move - bot_move) % 3
    # We do subtraction to find the difference between plr_move and bot_move. (We add 3 to make sure we don't get a negative number.)
    # Tied Example (3 + 2 - 2) % 3 = 0
    # Win Example (3 + 0 - 2) % 3 = 1
    # Lose Example (3 + 0 - 1) % 3 = 2

    print(f"Bot Picked: {MOVES[bot_move].capitalize()}")
    print("You Tied" if game_results == 0 else "You Won" if game_results == 1 else "You Lost")

    return game_results

def bestOf(x):
    plr_wins = 0
    bot_wins = 0

    while True:
        print(f"Best of {x}: {plr_wins}:{bot_wins}")

        game_results = rockPaperScissors()
        
        # Update the win counters based on the game result
        if game_results == 1:
            plr_wins += 1
        elif game_results == 2:
            bot_wins += 1
        
        if plr_wins == x or bot_wins == x:
            print(f"""You {'won the Game!' if plr_wins == x else 'lost the Game!' if bot_wins == x else ''}""")
            break

while True:
    print("Welcome to Rock Paper Scissors! Select a Gamemode:")
    print(GAME_OPTIONS)
    game_mode = None
    while not game_mode:
        try:
            user_int = int(input("-> "))
            game_mode = user_int
        except ValueError:
            print("ValueError: Invalid Input Value") # If the player's input isn't a integer (int()) the player will get a "Invalid Input Value" error

        os.system('cls' if os.name == 'nt' else 'clear')

        if game_mode == 0:
            exit() # Exit function
        elif game_mode == 1:
            rockPaperScissors()
        elif game_mode == 2 or game_mode == 3:
            bestOf(game_mode == 2 and 3 or 10) # If it's a Gamemode that has more than one round it runs the bestOf Function.
        else:
            print("Invalid Gamemode!")
