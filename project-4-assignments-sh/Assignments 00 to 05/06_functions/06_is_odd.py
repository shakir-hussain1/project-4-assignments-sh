# This function checks if a number is odd and returns True if it is.

def is_odd(num: int):
    reminder = num % 2
    return reminder == 1

def main():
    for i in range(10):
        if is_odd(i):
            print(i , "is odd")
        else:
            print(i , "is even")

if __name__ == "__main__":
    main()
