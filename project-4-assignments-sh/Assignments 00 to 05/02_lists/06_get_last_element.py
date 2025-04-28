# This program gets the last element of a list

def get_last_element(lst):
    print(lst[-1])
    
def get_lst():
    lst = []
    user_input = input("Enter a message to add in list : ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Enter a message to add in list : ")
    return lst 

def main():
    lst = get_lst()
    get_last_element(lst)
    
if __name__ == "__main__":
    main()    
   