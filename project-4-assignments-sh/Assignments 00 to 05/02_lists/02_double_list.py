# This program doubles the values in a list

def main():
    numbers :list[int] = [1, 2, 3, 4]


    for i in range(len(numbers)):
        index : int = numbers[i]
        numbers[i] = index * 2
    print(numbers)


if __name__ == "__main__":
    main()
