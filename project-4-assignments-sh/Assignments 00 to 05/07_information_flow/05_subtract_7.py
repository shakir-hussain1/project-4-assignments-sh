# This function subtracts 7 from the given number and returns the result.

def subtract_seven(num):
    num = num - 7
    return num

def main():
    num : int = 7
    num = subtract_seven(num)
    print("Answer should be zero : " , num)
    
if __name__ == "__main__":
    main()    