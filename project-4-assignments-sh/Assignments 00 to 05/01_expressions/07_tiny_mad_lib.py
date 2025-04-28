# Write a program which prompts the user for an adjective, then a noun, then a verb, and then prints a fun sentence with those words!

start_sentence : str = "Panaversity is fun. I learned to program and used Python to make my"

def main():
        
    adjective: str = input("Please type an adjective and press enter. ")
    noun: str = input("Please type a noun and press enter. ")
    verb: str = input("Please type a verb and press enter. ")

    print(start_sentence + adjective + " " + noun + " " + verb + "!")

if __name__ == "__main__":
    main()
