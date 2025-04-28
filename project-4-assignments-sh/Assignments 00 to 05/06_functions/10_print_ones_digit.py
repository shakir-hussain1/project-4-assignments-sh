# This function prints the ones digit of the given number using the modulo operator.

def ones_digit(num : int):
   print("The one digit is : ", num % 10)

def main():
   user_input = int(input("Please type a number: "))
   ones_digit(user_input)

if __name__ == "__main__":
   main()

