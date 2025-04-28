# This function checks if the number 'n' is within the range [low, high], inclusive.

def in_range(n , low , high ):
    if n >= low and n <= high:
        return True
    return False

def main():
    n_input = int(input("Enter a number : "))
    low_input = int(input("Enter the lower bound : "))
    high_input = int(input("Enter the upper bound : "))
    print(in_range(n_input, low_input, high_input))
    
if __name__ == "__main__":
    main()    
