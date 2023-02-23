#!/usr/bin/env python3

""" Hangman Game """

#Importing Modules
from time import sleep
import random
from hangman_data import word_list, logo, stages, win_logo
import os

def clear():
    """Clears the terminal screen"""
    os.system('clear')

def play_again():
    """Takes input from user, depending in the answer returns a True or False value"""
    while True:
        user_choice = input("Do you want to play another game? (yes or no) ").lower()
        if user_choice == 'yes':
            start()
            return True
        elif user_choice == 'no':
            print("Come play again next time!")
            return False
        else:
            print("That is not a valid response, try again! Please enter yes or no. ")
            sleep(1)
            clear()

def start():
    """Defines and initiates all the values"""
    global selected_word, word_length, lives, missed_letters, blanks
    #Selects a random word from hangman_data.py file 
    selected_word = random.choice(word_list)
    word_length = len(selected_word)
    missed_letters = []
    lives = 6
    # Matching the number of blanks to the length of the selected word
    blanks = ["_" for _ in range(word_length)]
    clear()
    print(logo)
    sleep(2)
    clear()

# main game loop
def main():
    global lives
    global missed_letters
    #First thing is defining the variables with the function start() so we can use them later
    start()
    end_of_game = False
    #Loop for the main game
    while not end_of_game:
        #Uses the delimeter ' ' to put a space between the blanks that we defined earlier
        print(f"{' '.join(blanks)}")
        #Prints the lives left in the form of hangman ascii art
        print(f"{stages[lives]}")
        #Displays a list of the wrong letters so the user doesn't try the same letter twice
        print(f"Missed Letters: {missed_letters}")
        #Ask user for a letter
        guess = input("Guess a letter: ").lower()
        clear()
        #Input validation to catch anything that is not 1 letter in the alphabet
        if len(guess) != 1 or guess.isalpha() == False:
            print("Invalid input, try 1 letter at a time!")
            continue
        #Checks to see if it's a repeated guess
        elif guess in blanks:
            print(f"You already guessed {guess}!")
        #Checks to see if the input is part of the selected word
        elif guess in selected_word:
            #For loop that compares the guess to every letter in the selected word
            for i in range(word_length):
                letter = selected_word[i]
                #If it finds a match, replaces the blank with the guess
                if letter == guess:
                    blanks[i] = letter
        #Checks to see if the guess is not in selected word
        elif guess not in selected_word:
            #Checks to see that the guess is not a letter than already exist in the list
            if guess not in missed_letters:
                missed_letters+= guess
            print(f"{guess} is not in the secret word!")
            lives -= 1
        #If there's not blanks left in the list, it can be assumed that the user won
        if "_" not in blanks:
            clear()
            print(win_logo)
            sleep(2)
            clear()
            #Ask to play again, returns True and False values
            if play_again():
                start()
                continue
            else:
                break
        #Checks to see if lives remmaining equal 0
        if lives == 0:
                print(f"{stages[lives]}")
                print("You ran out of lives, you lose!")
                if play_again():
                    start()
                    continue
                else:
                    break

if __name__ == "__main__":
    main()

