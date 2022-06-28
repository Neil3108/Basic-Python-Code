import sys
import math
import threading
import time
import random
from functools import reduce


def main():
    number = random.randint(1,100) # Random number
    guess = int(input("Enter your guess: ")) # User's guess

    while number != guess:
        if guess < number:
            print("Your guess is too low")
            guess = int(input("Enter your guess: "))
        else:
            print("Your guess is too high")
            guess = int(input("Enter your guess: "))
            
    if number == guess:
        print("Your guess is correct!")

main()
