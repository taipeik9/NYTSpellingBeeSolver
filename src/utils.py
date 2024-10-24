import os
import json
import time

import regex as re
import keyboard as kbd

letter_contain_dir = "./letter-contain-lists"

options = {
    1: "first",
    2: "second",
    3: "third",
    4: "fourth",
    5: "fifth",
    6: "sixth",
}


def print_header() -> None:
    print("=========================================")
    print("=========NYT Spelling Bee Solver=========")
    print("=========================================")


def get_input(allow_exit: bool = True) -> str:
    valid = False
    user_input = ""
    pattern = re.compile(f"^[A-Za-z{0 if allow_exit else ''}]$")

    while not valid:
        print(">>>", end=" ")
        user_input = input()

        if not pattern.match(user_input):
            print("Invalid input. Try Again.")
        else:
            valid = True

    return user_input


def enter_secondaries() -> str:
    secondaries = ""
    for i in range(6):
        print(f'Enter the {options[i + 1]} secondary letter. (Enter "0" to exit)')
        user_input = get_input()
        if user_input == "0":
            return "0"

        secondaries += user_input

    return secondaries


def open_letter_contain(letter: str) -> list[str]:
    with open(os.path.join(letter_contain_dir, f"{letter.lower()}-contain.json")) as f:
        words = json.load(f)
    return words


def contains(words: list[str], letters: str) -> list[str]:
    pattern = re.compile(f"^[{letters.lower()}]+$")
    return [word for word in words if pattern.match(word)]


def write_words(words: list[str]) -> None:
    write_words = "\n".join(words)

    print()
    print("=====================================================")
    print("You have three (3) seconds to switch back to the game!")
    time.sleep(3)

    kbd.write(write_words, 0.1)
