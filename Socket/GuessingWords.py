#!/usr/bin/env python3

"""
This program using socket to talk to Khoury server to play the guessing secred
word game.

HOST = 'proj1.3700.network'

marks meaning:
0: Letter does not appear in the secret word
1: Letter appears in the secret word, but not in this position
2: Letter appears in the secret word in this position
"""
import socket
import json
import random
import argparse
import ssl

PORT = 27993

def main():
    parser = argparse.ArgumentParser(description="port number, flag, hostname, NEU-username")

    parser.add_argument("-p", "--port", type=int, default=PORT,
                        help="the TCP port that the server is listening on")
    parser.add_argument("-s", action="store_true",
                        help="the client should use an TLS encryped socket connection")
    parser.add_argument("hostname", help="the name of the server(either a DNS" +
                        "name or an IP address in dotted notaion)")
    parser.add_argument("Northeastern_username", help="NEU usename")

    args = parser.parse_args()

    if (args.s):
        tls_socket(args.hostname, 27994, args.Northeastern_username)
        # if (args.port == 27993):
        #     tls_socket(args.hostname, 27994, args.Northeastern_username)
        # else:
        #     tls_socket(args.hostname, 27994, args.Northeastern_username)
    else:
        normal_socket(args.hostname, args.port, args.Northeastern_username)


#generate a tls socket
def tls_socket(host, port, user_name):
    # Connecting to the server:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with ssl.wrap_socket(sock) as ssock:
            connect_to_server(ssock, host, port, user_name)


# generate a normal socket
def normal_socket(host, port, user_name):
    # Connecting to the server:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        connect_to_server(s, host, port, user_name)


def connect_to_server(s, host, port, user_name):
    s.connect((host, port))
    print("here")
    # start the game:
    # ---------------
    start = {"type" : "hello", "northeastern_username": user_name}
    greeting(s, start)
    data = s.recv(1024)
    # storing game id
    game_id = json.loads(data.decode('utf-8'))['id']

    # makeing guesses
    # ---------------
    game_over = False
    # a dictionary representing 2-letters
    secret = {0:None, 1:None, 2:None, 3:None, 4:None}
    # a dictionary representing 1-letters
    possible_letters = {0:None, 1:None, 2:None, 3:None, 4:None}
    # a list keeps track of guessed words
    guessed_words = []
    # a list keeps track of letters that are not in the words
    letters_not_in_word = []
    # a list keeps track of letters that are in the words
    letters_in_word = []
    # this accumulator tracks the index of server "guesses" responses
    accu = 0;
    while(not game_over):
        print(letters_not_in_word)
        print(letters_in_word)
        word = next_guess(secret, possible_letters, guessed_words, letters_not_in_word, letters_in_word)
        guessed_words.append(word)
        guess = {"type": "guess", "id": game_id, "word": word}
        guessing(s, guess)
        data_2 = s.recv(1024)
        received = json.loads(data_2.decode('utf_8'))
        if (received['type'] == "bye"):
            print("\nflag: " + str(received['flag']))
            game_over = True
            break
        if (received['type'] == "error"):
            print("server error: " + received['message'])
            break
        word_from_server = received['guesses'][accu]['word']
        marks = received['guesses'][accu]['marks']
        accu += 1
        guess_update(secret, possible_letters, word, marks, letters_not_in_word, letters_in_word)
        print(word_from_server + " : " + str(marks))


# initialize the game:
def greeting(s, start):
    # greetingBytes = json.dumps(str(start) + "\n").encode('utf-8')
    # s.sendall(greetingBytes)
    greetingBytes = json.dumps(start).encode('utf-8')
    s.sendall(greetingBytes + b'\n')


# returns a random word from the words.txt
def next_guess(secret, possible_letters, guessed_words, letters_not_in_word, letters_in_word):
    words_file = open("words.txt")
    all_words = words_file.read().splitlines()

    empty = True
    for value in secret.values():
        if value is not None:
            empty = False

    # first guess or when all letters are wrong
    if (empty and len(possible_letters) == 0):
        return random.choice(all_words)

    # guessed something right
    for word in all_words:
        # make sure not guessing the same word again
        if word not in guessed_words:
            letters = [char for char in word]
            # make sure not guessing the letters that not in the word
            newLetters = True
            for l in letters_not_in_word:
                if l in letters:
                    newLetters = False
                    break
            for l in letters_in_word:
                if l not in letters:
                    newLetters = False
                    break

            if newLetters:
                # has 2 letters but not 1 letters
                if (not empty and len(possible_letters) == 0):
                    if (next_guess_dict_help(letters, secret)):
                        return word

                # has 1 letters but not 2 letters
                elif (empty and len(possible_letters) != 0):
                    if (next_guess_list_help(letters, secret, possible_letters)):
                        return word

                # has both 1 and 2 letters:
                else:
                    if (next_guess_dict_help(letters, secret) and
                        next_guess_list_help(letters, secret, possible_letters)):
                        return word
    words_file.close()


# check if the given letters contains the corresbonding letters in secret
def next_guess_dict_help(letters, secret):
    for key in secret.keys():
        if secret[key] is not None and letters[key] != secret[key]:
            return False
    return True


# check if the given letters contains all of the letters in possible_letters
def next_guess_list_help(letters, secret, possible_letters):
    remaining_letters = []
    copy_possible_letters = []
    for key in possible_letters.keys():
        if possible_letters[key] is not None:
            # when the 1 letter appear at the same possition return False
            if letters[key] == possible_letters[key]:
                return False
            copy_possible_letters.append(possible_letters[key])

    for i in range(5):
        if (secret[i] is None and possible_letters[i] is None):
            remaining_letters.append(letters[i])

    for l in copy_possible_letters:
        if l in remaining_letters:
            remaining_letters.remove(l)
        else:
            return False
    return True

# making a guess:
def guessing(s, guess):
    print(guess)
    guess_bytes = json.dumps(guess).encode('utf-8')
    s.sendall(guess_bytes + b'\n')


# update the accumulator accoding to the returned mark from server
def guess_update(secret, possible_letters, word, marks, letters_not_in_word, letters_in_word):
    letters = [char for char in word]
    # updating 2 letters
    for i in range(5):
        if (marks[i] == 2):
            secret[i] = letters[i]
            if (letters[i] not in letters_in_word):
                letters_in_word.append(letters[i])

    # updating 1 letters
    for i in range(5):
        if (marks[i] == 1):
            possible_letters[i] = letters[i]
            if (letters[i] not in letters_in_word):
                letters_in_word.append(letters[i])
        else:
            possible_letters[i] = None

    # updating 0 letters
    # worth it to set up for letters_not_in_word
    letter_in_secret = []
    letter_in_possible_letters = []
    for i in range(5):
        if secret[i] is not None:
            letter_in_secret.append(secret[i])
        if possible_letters[i] is not None:
            letter_in_possible_letters.append(possible_letters[i])

    for i in range(5):
        if (marks[i] == 0 and
            letters[i] not in letter_in_secret and
            letters[i] not in letter_in_possible_letters and
            letters[i] not in letters_not_in_word):
            letters_not_in_word.append(letters[i])

if __name__ == "__main__":
    main()
