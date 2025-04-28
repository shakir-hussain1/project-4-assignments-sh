# This program generate a secret random number and compare with users guess.

import random
from builtins import input, int, print

def main():
    secret_number = random.randint(1, 99)

    print("I'm thinking of a number between 1 and 99 ...")

    guess = int(input("Enter a guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")     
        print()
        guess = int(input("Enter a new guess: "))

    print("Congratulations! The number was :" + str(secret_number))

if __name__ == "__main__":
    main()

