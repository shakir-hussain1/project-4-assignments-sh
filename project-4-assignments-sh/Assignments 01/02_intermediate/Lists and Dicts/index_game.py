# This program helps practice list operations like accessing, modifying,
# and slicing elements through a simple interactive game.

def access_element(my_list, index):
    """
    Returns the element at the specified index in the list.
    If the index is out of range, returns an appropriate message.
    """
    if 0 <= index < len(my_list):
        return f"Element at index {index}: {my_list[index]}"
    else:
        return "Index out of range"

def modify_element(my_list, index, new_value):
    """
    Replaces the element at the specified index with a new value.
    If the index is out of range, returns an appropriate message.
    """
    if 0 <= index < len(my_list):
        my_list[index] = new_value
        return f"Element at index {index} has been changed to {new_value}."
    else:
        return "Index out of range"

def slice_list(my_list, start, end):
    """
    Returns a new list containing elements from the start index to the end index (exclusive).
    Handles cases where the indices are out of range.
    """
    if 0 <= start <= end <= len(my_list):
        return my_list[start:end]
    else:
        return "Invalid range"

def game():
    my_list = ["apple", "banana", "cherry", "date", "elderberry"]

    while True:
        print("\nCurrent list:", my_list)
        print("Select an operation:")
        print("1. Access an element")
        print("2. Modify an element")
        print("3. Slice the list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            try:
                index = int(input("Enter the index to access: "))
                result = access_element(my_list, index)
                print(f"Result: {result}")
            except ValueError:
                print("Please enter a valid integer for the index.")
        
        elif choice == "2":
            try:
                index = int(input("Enter the index to modify: "))
                new_value = input("Enter the new value: ")
                result = modify_element(my_list, index, new_value)
                print(f"Result: {result}")
            except ValueError:
                print("Please enter a valid integer for the index.")

        elif choice == "3":
            try:
                start_index = int(input("Enter the start index: "))
                end_index = int(input("Enter the end index: "))
                result = slice_list(my_list, start_index, end_index)
                print(f"Result: {result}")
            except ValueError:
                print("Please enter valid integers for the indices.")

        elif choice == "4":
            print("Exiting the game.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    game()
