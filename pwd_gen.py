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
        self.non_nouns = get_words("non_nouns")
        self.colors = get_words("colors")

    def generate_password(self):
        color = get_random_word(self.colors)
        noun = get_random_word(self.nouns)
        non_noun = get_random_word(self.non_nouns)
        digits = get_random_digits(2)
        password = (noun, color, non_noun, digits)
        return joiner(choice([i for i in permutations(password)]))
    
    def generate_passwords(self, number=1):
        return [self.generate_password() for i in range(number)]
    
if __name__ == "__main__":
    try:
        number_of_passwords = int(sys.argv[1])
    except (KeyError, ValueError) as error:
        print("Defaulting to 10 passwords because of the following error: ", error, "\n")
        number_of_passwords = 10
    print(f"Here are {number_of_passwords} password suggestions for you...")
    generator = Generator()
    print(generator.generate_passwords(number_of_passwords))
