from random import randint
import os

MOVES = ["rock", "paper", "scissors"]

GAME_OPTIONS = """
====================
0: Exit
1: Play
====================
"""

MOVE_OPTIONS = """
====================
Rock
Paper
Scissors
====================
"""

def game():
    print("Choose:", MOVE_OPTIONS)

    user_input = input("-> ").lower()

    if not user_input in MOVES:
        print("Invalid Move")
        return
    
    plr_move = MOVES.index(user_input)
    bot_move = randint(0, 2)

    results = (3 + plr_move - bot_move) % 3
    # We do subtraction to find the difference between plr_move and bot_move. (We add 3 to make sure we don't get a negative number.)

    print(f"Bot Picked: {MOVES[bot_move].capitalize()}")
    print("You Tied" if results == 0 else "You Won" if results == 1 else "You Lost")

while True:
    game_mode = None
    while not game_mode:
        try:
            print(GAME_OPTIONS)
            user_int = int(input("-> "))
            game_mode = user_int
        except ValueError:
            print("ValueError: Invalid Input Value") # If the player's input isn't a integer (int()) the player will get a "Invalid Input Value" error

    if game_mode == 0:
        exit()
    elif game_mode == 1:
        game()
