# This function checks if the given age is greater than or equal to the legal adult age (18).


ADULT_AGE = 18

def is_adult(age : int):
    if age >= ADULT_AGE:
        return True
    return False

def main():
    age:str = int(input("Enter your age: "))
    print(is_adult(age))

if __name__ == "__main__":
    main()

