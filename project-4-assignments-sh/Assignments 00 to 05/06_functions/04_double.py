# This program ask for a int input and return its double number

def double(num: int) :
    return num *2 

def main():
    print("Double the number")
    num = int(input("Enter a number: "))
    num_doubled = double(num)
    print(f"Double that is", num_doubled)

if __name__ == "__main__":
    main()

