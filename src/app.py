from utils import (
    print_header,
    get_input,
    enter_secondaries,
    open_letter_contain,
    contains,
    write_words,
)

if __name__ == "__main__":
    print_header()

    while True:
        secondaries = ""
        print()
        print('Enter the primary letter. (Enter "0" to exit)')

        primary = get_input()
        if primary == "0":
            break

        secondaries = enter_secondaries()
        if secondaries == "0":
            break

        primary_words = open_letter_contain(primary)
        words = contains(words=primary_words, letters=primary + secondaries)

        write_words(words=words)

    print("Thanks for playing! Goodbye!")
