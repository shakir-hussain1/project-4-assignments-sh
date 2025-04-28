# This program ask for message from user and make its 3 copies and append in list this show the mutability of list

def three_copies(my_list, data):
    for i in range(3):
        my_list.append(data)
        
def main():
    print("Making three copies of message")
    user_input = input("Enter a message to copy : ")
    my_list = []
    print(f"Before List : {my_list}")
    three_copies(my_list, user_input)
    print(f"After List : {my_list}")
    
if __name__ == "__main__":
    main()    
