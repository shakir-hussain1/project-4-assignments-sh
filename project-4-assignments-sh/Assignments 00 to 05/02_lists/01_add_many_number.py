# Write a function that takes a list of numbers and returns the sum of those numbers.

def add_many_numbers(numbers) -> int :
    many_numbers: int = 0
    for number in numbers:
        many_numbers += number
    return many_numbers

def main():
    numbers : list[int] = [1, 2, 3, 4, 5]
    sum_of_numbers  : int = add_many_numbers(numbers)
    print(f"The sum of the numbers is : {sum_of_numbers}")

if __name__ == "__main__":
    main()

