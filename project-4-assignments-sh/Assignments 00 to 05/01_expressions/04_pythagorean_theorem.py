#This program asks the user for lengths of the two perpendicular sides of a right triangle and outputs the length of the third side (the hypotenuse) using the Pythagorean theorem!


import math  

def main():
    ab: float = float(input("Enter the length of AB: "))
    ac: float = float(input("Enter the length of AC: "))

    bc: float = math.sqrt(ab**2 + ac**2)
    print("The length of BC (the hypotenuse) is: " + str(bc))



if __name__ == '__main__':
    main()