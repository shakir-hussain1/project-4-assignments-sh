# This function collects the user's first name, last name, and email and returns them as a tuple.

def get_user_data():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print("Received user data:", user_data)

if __name__ == "__main__":
    main()
