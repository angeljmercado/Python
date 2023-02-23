#!/usr/bin/env python3

from time import sleep
while True:
    user= input("How many beers you going to be drinking?")
    user= int(user)
    if user <= 0 or user >= 100:
        print("Don't go past 100! Try again")
        continue
    for n in range(user, 0, -1):
        print(f"{n} bottles of beer on the wall! {n} bottles of beer! You take one down, pass it around! {n} bottles of beer!")
        sleep(0.3)
    
    