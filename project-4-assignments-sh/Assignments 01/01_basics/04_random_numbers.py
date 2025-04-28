# This program generates and prints 10 random numbers between 1 and 100 each time it runs.

import random

N_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100

def main():
    print("Generate and print 10 random numbers between 1 and 100")
    for i in range(N_NUMBERS):
        random_number: int = random.randint(MIN_VALUE, MAX_VALUE)
        print(random_number)

if __name__ == "__main__":
    main()
