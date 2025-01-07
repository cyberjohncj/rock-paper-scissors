from random import randint

rules = ["Rock", "Paper", "Scissors"]

def start_round():
    u1 = None
    while not u1 in rules:
        u1 = str(input("Rock, Paper, or Scissors? : ")).capitalize()
    u1 = rules.index(u1)
    bots_move = randint(0,2)
    print(f"Bot Picked: {rules[bots_move]}")
    return (u1 - bots_move) % 3

while True:
    points = 0
    print("Rock Paper Scissors Best of 3")
    for i in range(0, 3):
        winner_of_round = start_round()
        if winner_of_round == 0:
            print("Tied Game")
        elif winner_of_round == 1:
            points += 1
            print("You Won")
        else:
            print("You Lost")

        print(f"{points}:{}")
        
        if (i == 1 or i == 2) and points == 2:
            print("Congrats! You Win")
            break
        elif i == 2 and points < 2:
            print("You Lose :(")
            break

    u_continue = None
    while not u_continue in ["Y", "N"]:
        u_continue = str(input("Continue? [Y, N]")).capitalize()
    if not u_continue == "Y":
        break
print("Bye, Thanks for Playing!")
