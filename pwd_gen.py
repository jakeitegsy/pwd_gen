#! usr/bin/env python
""" 
Password Generator
    Creates an Alpha numeric password using this combination
        - present continuous verb e.g. Reading
        - noun e.g Giraffe
        - random 2 digit number
    i.e.
        <verb>ing<noun><digitn-1><digitn>
        ReadingGiraffe42
"""
import string
from secrets import choice
from itertools import permutations

def random_digit():
    digits = string.digits
    return choice(digits)

def random_color():
    colors =("Red", "Orange", "Yellow", "Green", "Cyan", 
             "Blue", "Indigo", "Violet")
    return choice(colors)
    
def random_noun():
    with open("nouns.txt") as f:
        noun_list = f.readlines()
        
    return choice(noun_list).strip(" \n").title()
    
def random_verb():
    """Return a verb in the present continuous i.e. -ing form"""
    with open("verbs.txt") as f:
        verb_list = f.readlines()
    return choice(verb_list).strip(" \n").title()
    
def random_order():
    color = random_color()
    noun = random_noun()
    verb = random_verb()
    digits = f"{random_digit()}{random_digit()}"
    password = (f"{noun}", f"{color}", f"{verb}")
    number = choice((2, 3))
    possibilities = [i for i in permutations(password, number)]
    
    if number == 2:
        first, second = choice(possibilities)
        final = [i for i in permutations((first, second, digits), 3)]
        first, second, third = choice(final)
        return f"{first}{second}{third}"
    else:
        first, second, third = choice(possibilities)
        final = [i for i in permutations((first, second, third, digits), 4)]
        first, second, third, fourth = choice(final)
        return f"{first}{second}{third}{fourth}"

def generate_password():
    """Return a password of the form ColorNounVerbDigitDigit in random order except for digits at the end"""
    print(f"{random_order()}")
    
if __name__ == "__main__":
    print("Here's a password suggestion for you...")
    generate_password()
