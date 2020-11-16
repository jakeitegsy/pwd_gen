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
            return list(set(file.readlines()))

    def get_random_word(self, list):
        return "".join(choice(list).title().strip().split())

    @staticmethod
    def get_random_digits(number=4):
        return "".join(choice(string.digits) for i in range(number))

    def generate_password(self):
        color = get_random_word("colors")
        noun = get_random_word("nouns")
        non_noun = get_random_word("non_nouns")
        digits = get_random_digits()
        password = (noun, color, non_noun, digits)
        return "".join(choice([i for i in permutations(password)]))
    
    def generate_passwords(self, number):
        return [generate_password() for i in range(number)]
    
if __name__ == "__main__":
    print("Here are 20 password suggestions for you...")
    generator = Generator()
    generator.generate_passwords(20)
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
            return list(set(file.readlines()))

    def get_random_word(self, list):
        return "".join(choice(list).title().strip().split())

    @staticmethod
    def get_random_digits(number=4):
        return "".join(choice(string.digits) for i in range(number))

    def generate_password(self):
        color = get_random_word("colors")
        noun = get_random_word("nouns")
        non_noun = get_random_word("non_nouns")
        digits = get_random_digits()
        password = (noun, color, non_noun, digits)
        return "".join(choice([i for i in permutations(password)]))
    
    def generate_passwords(self, number):
        return [generate_password() for i in range(number)]
    
if __name__ == "__main__":
    print("Here are 20 password suggestions for you...")
    generator = Generator()
    generator.generate_passwords(20)
