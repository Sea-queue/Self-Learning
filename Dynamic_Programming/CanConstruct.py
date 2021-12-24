"""
Write a function 'canConstruct(target, wordBank)' that accepts a target string
and an array of strings.

The function should return a boolean indicating whether or not the 'target'
can be constructed by concatenating elements of the 'wordBank' array.

you may reuse elements of 'wordBank' as many times as needed.
("staketboard" ["sta", "ake", "board"]) --> false
("", ["cat", "dog"]) --> true
"""

def canConstruct(target, wordBank):
    if target == "":
        return True

    for word in wordBank:
        if (len(word) <= len(target)):
            sub = target[0:len(word)]
            if (sub == word):
                if (canConstruct(target[len(word):], wordBank)):
                    return True

    return False


#Dynamic programming using memoization:
def canConstructDP(target, wordBank, table):
    if target in table:
        return table[target]
    if target == "":
        return True

    for word in wordBank:
        if len(word) <= len(target):
            prefix = target[0:len(word)]
            if prefix == word:
                sub = target[len(word):]
                if canConstructDP(sub, wordBank, table):
                    table[sub] = True
                    return True

    table[target] = False
    return False


print(canConstruct("abc", ["ab", "c"]))
print(canConstruct("abcd", ["a", "cd", "bc"]))
print(canConstructDP("eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee"], dict()))
