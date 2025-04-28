# This program adds two numbers

def main():
    print("This program adds two numbers.")
    num1 : str = input("Enter the first number: ")
    num1 : int = int(num1)
    num2 : str = input("Enter the second number: ")
    num2 : int = int(num2)
     # Calculate sum
    total :int = num1 + num2
      # Display result
    print(f"The total is {total}.")


# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()