# This function checks how many fruits of a given type are in stock and returns that number.

def num_in_stock(fruit : str):
    if fruit == "apple":
        return 2
    elif fruit == "orange":
        return 4
    elif fruit == "banana":
        return 6
    else: 
        return 0
    
def main():
    fruit_input = input("Enter a fruit: ")
    stock = num_in_stock(fruit_input)
    if stock == 0 :
        print("Sorry, we don't have that fruit in stock.")
    else:
        print("We have", stock, "of that fruit in stock.")

if __name__ == "__main__":
    main()
