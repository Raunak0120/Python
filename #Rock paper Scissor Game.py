#Rock paper Scissor Game

import random

options = ("rock", "paper", "scissor")
player = None
computer = random.choice(options)
running = True
while running:

    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Choose A choice (Rock, Paper, Scissor): ") 

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("!! Tie !!")
    elif player == "rock" and computer == "scissor":
        print("!! You Win !!")
    elif player == "scissor" and computer == "paper":
        print("!! You Win !!")
    elif player == "paper" and computer == "rock":
        print("!! You Win !!")
    else:
        print("!! You Loose !!")

        if not input("Play again (y/n): ").lower() == "y":
            running = False

print("!! Thanks For Playing !!")