# This function takes a name as input and returns a greeting message.

def greet(name : str):
    return "Greetings, " + name + "!"
    
def main():
    user_name = input("Please type your name : ")    
    print(greet(user_name))
    
if __name__ == "__main__":
    main()    
    
    