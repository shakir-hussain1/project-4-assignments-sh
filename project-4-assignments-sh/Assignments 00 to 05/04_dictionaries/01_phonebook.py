# This program show an example of using dictionaries to keep track of information in a phonebook.

def read_phone_numbers():

    phonebook = {}

    while True:
        name = input("Enter a name: ")
        if name == "":
            break
        number = input("Enter a phone number: ")
        phonebook[name] = number
    return phonebook

def print_phonebook(phonebook):

    for name in phonebook :
        print(str(name) + " : " + str(phonebook[name]))

def lookup_number(phonebook):

    while True:
        name = input("Enter name to lookup: ")
        if name == "" :
            break
        if name not in phonebook :
            print(name + "is not in the phonebook")
        else:
            print(phonebook[name])

def main():
    phonebook = read_phone_numbers()
    print_phonebook(phonebook)
    lookup_number(phonebook)

    

if __name__ == "__main__":
    main()

