#!/usr/bin/env python3

"""Game about guessing a random number"""
import os
import random
from time import sleep
def clear():
    os.system('clear')

print("""    _______________________ 
            |  ___________________  |
            | | Guess the Number! | |
            | |___________________| |
            |_______________________|  """)
sleep(1)
clear()

lives= 5
random_number = random.randint(1,100)

def guess_game():
    global lives
    #Input validation for numbers out of our desired range
    if user_guess == 0 or user_guess > 100:
        print("That's not a valid number within the 1 to 100 range")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    #Compare User Guess to the Random Number
    elif user_guess == random_number:
        print(f"Number is {user_guess} you win!")
        again()
    #If user guess is greater than number, substract 1 life
    elif user_guess > random_number:
        lives -= 1
        print("Too High!")
        print(f"You have {lives} attempts remaining to guess the number.")
    #If user guess is less than number, substract 1 life
    elif user_guess < random_number:
        lives -= 1
        print("Too Low!")
        print(f"You have {lives} attempts remaining to guess the number.")
    

def again():
    global lives
    global should_continue
    global random_number
    user_answer= input("Do you want to play another game 'yes' or 'no': ").lower()
    if user_answer == 'yes':
        lives= 5
        random_number = random.randint(1,100)
        clear()
    elif user_answer == "no":
        clear()
        print("Come play next time!")
        should_continue= False
    else:
        clear()
        print("That's not a valid response")
        print("Come play again next time!")
        should_continue= False

def game_over():
    global lives
    if lives == 0:
        print("You've run out of lives, you lose.")
        again()

should_continue = True
while should_continue:
    #print(random_number)-The secret number for debugging
    print("I am thinking of a number between 1 and 100.") 
    sleep(0.5)
    user_guess = input("Make a Guess: ")
    try:#Verify if user input is a Integer, if not use Except
        user_guess= int(user_guess)
    except:#Catches any string, and starts the loop again using "continue"
        print("That is not a valid input Dum Dum! Only numbers from 1 to 100")
        print(f"You have {lives} attempts remaining to guess the number.")
        sleep(2)
        clear()
        game_over()
        continue
    guess_game()
    game_over()
