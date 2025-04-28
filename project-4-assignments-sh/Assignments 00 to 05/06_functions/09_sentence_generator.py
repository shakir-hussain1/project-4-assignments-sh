# This function generates a sentence based on the word and its part of speech (noun, verb, or adjective).


def mak_sentence(word , part_of_speech):
    if part_of_speech == 0:
        #noun
        print("I am excited to add this " + word + " to my vast collection of them!")
    elif part_of_speech == 1:
        #verb
        print("It's so nice outside today it makes me want to " + word + "!")
    elif part_of_speech == 2:
        #adjective
        print("Looking out my window, the sky is big and " + word + "!")
    else:
        print("Part of speech must be 0, 1, or 2! Can't make a sentence.")

def main():
    word :str = input("Please type a noun, verb, or adjective:")
    print("It this a noun, verb or adjective?")
    part_of_speech :int = int(input("Enter 0 for noun, 1 for verb, 2 for adjective:"))
    mak_sentence(word, part_of_speech)

if __name__ == "__main__":
    main()
