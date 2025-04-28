# This program generate and print the Fibonacci sequence up to a maximum value of 10,000.
MAX_TERM_VALUE = 10000

def main():
    current_term = 0  
    next_term = 1  
    while current_term <= MAX_TERM_VALUE:
        print(current_term) # type: ignore
        term_after_next = current_term + next_term
        current_term = next_term
        next_term = term_after_next



if __name__ == '__main__':
    main()
    
    