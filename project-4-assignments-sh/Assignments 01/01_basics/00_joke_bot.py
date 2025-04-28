# This is a simple joke bot that tells a joke when asked for one.
PROMPT: str = "What do you want? "
JOKE: str = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs'"
SORRY: str = "Sorry I only tell jokes."

def main():
    user_input: str = input(PROMPT)
    
    if "joke" in user_input:
        print(JOKE)
    else:
        print(SORRY)

if __name__ == "__main__":
    main()
