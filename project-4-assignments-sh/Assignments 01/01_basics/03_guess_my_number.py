# This program lets the user guess a randomly chosen number between 1 and 99, providing feedback until they guess correctly.

import random
def main():

    secret_number: int = random.randint(1, 99)

    print("I'm thinking of a number between 1 and 99.")

    guess = int(input("Enter your guess: "))

    while guess != secret_number:
        if guess < secret_number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")
        
        print()
        guess: int = int(input("Enter a new guess: "))        

    print("Congratulations! The number was: " + str(secret_number))

if __name__ == "__main__":
    main()
