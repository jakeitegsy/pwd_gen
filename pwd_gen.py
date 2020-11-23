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


class Generator:

    def __init__(self):
        self.nouns = get_words("nouns")
        self.others = get_words("others")
        self.colors = get_words("colors")

    def generate_password(self):
        #colors = ("Red", "Orange", "Green", "Yellow", "Blue", "Indigo", "Violet")
        #color = get_random_word(colors)
        color = get_random_word(self.colors)
        noun = get_random_word(self.nouns)
        other = get_random_word(self.others)
        digits = get_random_digits(4)
        password = (
            noun,
            color,
            other,
            digits
        )
        return joiner(choice([i for i in permutations(password)]))
    
    def generate_passwords(self, number=1):
        return [self.generate_password() for i in range(number)]
    
if __name__ == "__main__":
    number_of_passwords = 10
    try:
        number_of_passwords = int(sys.argv[1])
    except (ValueError, IndexError):
        print("Defaulting to 10 passwords:\n")
    finally:
        print(f"Here are {number_of_passwords} password suggestions for you...")
        generator = Generator()
        print(generator.generate_passwords(number_of_passwords))
