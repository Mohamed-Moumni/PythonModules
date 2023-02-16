import sys
import random


print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit'to end the game.\nGood luck!")

number = random.randint(1, 99)
count = 0
while True:
    guess = input("What's your guess between 1 and 99?")
    if not (guess.isnumeric()):
        print("The input is not an integer")
    else:
        if int(guess) == number:
            print("Congratulations, you've got it!")
            if int(guess) == 42:
                print("The answer to the ultimate question of life, the universe and everything is 42.")
            if count == 0:
                print("Congratulations! You got it on your first try!")
            else:
                print(f"You won in {count} attempts!")
            break
        elif int(guess) < number:
            print("Too low!")
        elif int(guess) > number:
            print("Too High!")
        elif guess == "exit":
            print("Goodbye!")
    count += 1