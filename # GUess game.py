# Guess game

import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("Python : Number Guessing Game")
print(f"Select a Number Between {lowest_num} & {highest_num}")

while is_running:

    guess = input("Enter Your Guess: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("The number is ou of range")
            print(f"Select a Number Between {lowest_num} & {highest_num}")

        elif guess < answer:
            print("Too Low !! Try Again")
        elif guess > answer:
             print("Too High !! Try Again")

        else:
            print(f"Correct: The answer was {answer}")
            print(f"No.of guesses: {guesses}")
            is_running = False

  
    else:
        print("Invalid Guess")
        print(f"Select a Number Between {lowest_num} & {highest_num}")
