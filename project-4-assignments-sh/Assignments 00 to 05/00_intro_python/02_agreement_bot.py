# This program asks the user for their favorite animal and prints a message
def main():
    print("Favorite Animal")
    input_user :str = input("What is your favorite animal? ")
    print(f"My favorite animal is also \033[1m{input_user}!")


if __name__ == '__main__':
    main()