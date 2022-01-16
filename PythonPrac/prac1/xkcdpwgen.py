# Code written by Jackson Williams and Seaqueue (Cheng Qian)

import argparse
import random

# Password Option Constants
SYMBOLS = "~!@#$%^&*.:;"
DICTIONARY_FILE_NAME = "./words.txt"
DEFAULT_WORDS = 4
DEFAULT_CAPS = 0
DEFAULT_NUMBERS = 0
DEFAULT_SPECIAL_CHARS = 0


def xkcdpwgen():
    """
    Main entry method. Generates a password given options for a number of words,
    how many words to randomly capitilize, how many random numbers to include,
    and how many random special characters to include.
    """
    parser = argparse.ArgumentParser(prog='xkcdpwgen', description='Possible Variations of passwords:')

    parser.add_argument('-w', "--words", metavar="WORDS", type=int, default=DEFAULT_WORDS,
                        help="include WORDS word in the password (default=4)")
    parser.add_argument('-c', "--caps", type=int, metavar="CAPS", default=DEFAULT_CAPS,
                        help="capitalize the first letter of CAPS random words (default=0)")
    parser.add_argument('-n', "--numbers", type=int, metavar="NUMBERS", default=DEFAULT_NUMBERS,
                        help="insert NUMBERS random numbers in the password (default=0)")
    parser.add_argument('-s', "--symbols", type=int, metavar="SYMBOLS", default=DEFAULT_SPECIAL_CHARS,
                        help="insert SYMBOLS random symbols in the password (default=0)")

    args = parser.parse_args()

    if args.caps > args.words:
        parser.error("Number of capitals cannot be greater than the number of words.")

    random_words_list = get_random_words(args.words)
    capitilize_random_characters(random_words_list, args.caps)
    insert_random_numbers(random_words_list, args.numbers)
    insert_random_specials(random_words_list, args.symbols)

    print("".join(random_words_list))


def get_random_words(num_words):
    """
    Given a number of words, returns a list of random words from a dictionary
    large file.
    """
    words_file = open(DICTIONARY_FILE_NAME)
    all_words = words_file.read().splitlines()
    random_words = []
    for _ in range(num_words):
        random_words.append(random.choice(all_words))
    words_file.close()
    return random_words


def capitilize_random_characters(list_of_words, caps):
    """
    Given a list of words and a number of words to capitilize, capitilize random words
    in the list.
    """
    indices_used = set()
    for _ in range(caps):
        next_index = get_next_index(len(list_of_words) - 1, indices_used)
        list_of_words[next_index] = list_of_words[next_index].capitalize()


def get_next_index(upper_bound, indices_used):
    """
    Given an upper bound and a list of indices used, return an index that is not in
    the set.
    """
    next_index = random.randint(0, upper_bound)
    while next_index in indices_used:
        next_index = random.randint(0, upper_bound)
    indices_used.add(next_index)
    return next_index


def insert_random_numbers(list_of_words, nums):
    """
    Given a list of words and an amount of numbers, add digits at the beginning or end of a random
    word.
    """
    for _ in range(nums):
        random_number = str(random.randint(0, 9))
        insert_character_randomly(list_of_words, random_number)


def insert_random_specials(list_of_words, specials):
    """
    Given a list of words and an amount of special characters, adds a special character
    to the beginning or the end of random words. Does this as many times as specified
    by the amount.
    """
    for _ in range(specials):
        random_index = random.randint(0, specials - 1)
        insert_character_randomly(list_of_words, SYMBOLS[random_index])


def insert_character_randomly(list_of_words, character):
    """
    Given a list of words and a character, appends the character randomly to the beginning or end
    of a random word.
    """
    random_index = random.randint(0, len(list_of_words) - 1)
    # Choose randomly between beginning and end of the word. Beginning is 0,
    # end is 1.
    location_in_word = random.randint(0, 1)
    if location_in_word == 0:
        list_of_words[random_index] = character + list_of_words[random_index]
    else:
        list_of_words[random_index] = list_of_words[random_index] + character


if __name__ == "__main__":
    xkcdpwgen()
