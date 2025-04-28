
# Write a program which prompts the user to type an affirmation of your choice until they type it correctly

Affirmation : str = "I am capable of doing anything I put my mind to."

def main():
    print("Please type the following affirmation : " + Affirmation)
    user_input = input()
    while user_input != Affirmation:
        print("That was not the affirmation❗")
        print("Please type the following affirmation : " + Affirmation)
        user_input = input()
    print("That's right! :)")   
    
if __name__ == "__main__":
    main()     
