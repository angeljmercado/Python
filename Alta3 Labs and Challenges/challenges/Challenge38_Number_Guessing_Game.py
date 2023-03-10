#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""
import random

def main():
    num= random.randint(1,100)

    rounds= 0

    while rounds < 5:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit():
            guess= int(guess)
        else:
            continue

        if guess > num:
            print("Too high!")
            rounds+= 1
            if rounds == 5:
                print("You ran out of chances!")
                if input("Want to play again") == "yes".lower():
                    rounds= 0
                    continue
                else:
                    break
            
        if guess < num:
            print("Too low!")
            rounds+= 1
            if rounds == 5:
                print("You ran out of chances!")
                if input("Want to play again") == "yes".lower():
                    rounds= 0
                    continue
                else:
                    break
                
        else:
            print("Correct!")
            if input("Want to play again: ") == "yes".lower():
                rounds= 0
                continue
            else:
                break

if __name__ == "__main__":
    main()
    