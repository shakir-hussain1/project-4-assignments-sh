# This program asks user to enter a number then double that number and print out the result. It will repeat that process until the value is 100 or greater.

def main():
    current_value: int = int(input("Enter a number: "))

    while current_value < 100:
        current_value *= 2 
        print(current_value)

if __name__ == "__main__":
    main()
