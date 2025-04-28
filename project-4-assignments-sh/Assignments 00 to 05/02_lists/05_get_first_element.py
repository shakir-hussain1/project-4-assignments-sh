# This program gets the first element of a list

def get_first_element(lst):
    print(lst[0])
    
def get_lst():
    lst = []
    input_element = input("Enter element to add in list : ")
    while input_element != "":
        lst.append(input_element)
        input_element = input("Enter element to add in list : ")
    return lst

def main():
    lst = get_lst()
    get_first_element(lst)
    
if __name__ == "__main__":
    main()    
        