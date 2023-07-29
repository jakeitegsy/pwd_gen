#! usr/bin/env python
"""
Password Generator
    Creates an Alpha numeric password from a permutation of
        - non-noun e.g. Reading
        - noun e.g Giraffe
        - color e.g. Blue
        - random 2 digit number
    i.e.
        <non-noun><color><noun><digitn-1><digitn>
        ReadingBlueGiraffe42
"""
import string
import sys

from secrets import choice
from itertools import permutations

def get_words(filename):
    with open(f"{filename}.txt") as file:
        return list(set([word.strip() for word in file]))

def joiner(collection):
    return "".join(collection)

def get_random_word(words):
    return joiner(choice(words).title().split())

def get_random_digits(number=4):
    return joiner(choice(string.digits) for i in range(number))

def get_random_symbol():
    return joiner(choice('!@#$'))


class Generator:

    def __init__(self):
        self.nouns = get_words("nouns")
        self.others = get_words("others")
        self.colors = get_words("colors")

    def choices(self):
        return (
            get_random_word(self.colors),
            get_random_word(self.nouns),
            # get_random_word(self.others),
            get_random_digits(2),
            get_random_symbol()
        )


    def generate_password(self):
        return joiner(
            choice(
                [
                    password for password in
                    permutations(self.choices())
                ]
            )
        )

    def generate_passwords(self, number=1):
        result = []
        while len(result) < number:
            password = self.generate_password()
            if len(password) > 14:
                result.append(password)
        return result

if __name__ == "__main__":
    number_of_passwords = 10
    try:
        number_of_passwords = int(sys.argv[1])
    except (ValueError, IndexError):
        print("Defaulting to 10 passwords:\n")
    finally:
        print(f"Here are {number_of_passwords} password suggestions for you...")
        generator = Generator()
        for password in generator.generate_passwords(number_of_passwords):
            print(password)
