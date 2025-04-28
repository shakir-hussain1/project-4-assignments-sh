# This program squares a number

def main():
    print("square of number")
    try: 
        num : float = float(input("Enter a number to see it squared: "))
        print(str(num) + "Squared is " + str(num ** 2) )
    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ ==  '__main__':
    main()