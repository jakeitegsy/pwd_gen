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

from secrets import choice
from itertools import permutations

class Generator:

    def __init__(self):
        self.nouns = self.get_words("nouns")
        self.non_nouns = self.get_words("non_nouns")
        self.colors = self.get_words("colors")

    def get_words(self, filename):
        with open(f"{filename}.txt") as file:
            return list(set([word.strip() for word in file]))

    def get_random_word(self, words):
        return "".join(choice(words).title().strip().split())

    @staticmethod
    def get_random_digits(number=4):
        return "".join(choice(string.digits) for i in range(number))

    def generate_password(self):
        color = self.get_random_word(self.colors)
        noun = self.get_random_word(self.nouns)
        non_noun = self.get_random_word(self.non_nouns)
        digits = self.get_random_digits(2)
        password = (noun, color, non_noun, digits)
        return "".join(choice([i for i in permutations(password)]))
    
    def generate_passwords(self, number=1):
        return [self.generate_password() for i in range(number)]
    
if __name__ == "__main__":
    print("Here are 20 password suggestions for you...")
    generator = Generator()
    generator.generate_passwords(20)
