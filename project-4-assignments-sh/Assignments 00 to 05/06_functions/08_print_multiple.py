# This function prints the given message a specified number of times.

def print_multiples(message : str , repeats : int):
    for i in range(repeats):
        print(message)

def main():
    message = str(input("Enter a message : "))
    repeats = int(input("Enter the number of times to repeat : "))
    print_multiples(message, repeats)

if __name__ == "__main__":
    main()
