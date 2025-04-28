# This program shortens a list

max_length = 3

def shorten(lst):
    while len(lst) > max_length:
        pop_elem = lst.pop()
        print(pop_elem)
        
def get_list():
    lst = []
    user_input = input("Enter your value : ")
    while user_input != "":
        lst.append(user_input)
        user_input = input("Enter your value : ")
    return lst

def main():
    lst = get_list()
    shorten(lst)            

if __name__ == "__main__":
    main()
