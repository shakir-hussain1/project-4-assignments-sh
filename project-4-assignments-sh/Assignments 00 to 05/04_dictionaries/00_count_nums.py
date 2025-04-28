# This program counts the number of times each number appears in a list of numbers.

def get_user_number():
    user_number = []
    while True:
        user_input = input("Enter a number: ")
        if user_input == "":
            break
        num = int(user_input)
        user_number.append(num)
    return user_number

def count_numbers(num_lst):
    num_dict = {}
    for num in num_lst:
        if num in num_dict:
            num_dict[num] += 1
        else:
            num_dict[num] = 1
    return num_dict

def print_counts(num_dict):
    for num in num_dict:
        print(str(num) + " appears " + str(num_dict[num]) + " times.")

def main():
    user_numbers = get_user_number()
    num_dict = count_numbers(user_numbers)
    print_counts(num_dict)  # This was missing too!

main()
