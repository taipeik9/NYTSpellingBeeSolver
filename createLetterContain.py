# This script is not used in the application, its simply there to convert the
# txt dictionary file into the "letter contain lists" which are used in the application

import os
import json

import regex as re

ALPHABET = (
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
)

word_list_directory = "./word-lists-csv"


def create_letter_contain(letter: str, data: iter, directory: str) -> None:
    letter_data = []

    for word in data:
        if letter in word:
            letter_data.append(word)

    with open(os.path.join(directory, f"{letter}-contain.json"), mode="w") as f:
        json.dump(sorted(letter_data), f)


def clean_data(data: list) -> set:
    data = [word.strip() for word in data]
    pattern = re.compile(r"^[a-z]+$")
    data = [word for word in data if pattern.match(word)]

    data = [word for word in data if len(word) >= 4 and len(word) <= 7]

    return set(data)


if __name__ == "__main__":
    with open("./words_alpha.txt") as f:
        lines = f.read().splitlines()

    data_set = clean_data(lines)

    for letter in ALPHABET:
        create_letter_contain(letter, data=data_set, directory="./letter-contain-lists")

    print("Letter Contains Created Successfully")
