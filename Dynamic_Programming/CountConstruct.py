"""
Write a function 'countConstruct(target, wordBank)' that accepts a target string
and an array of strings

The function should return the number of ways that the 'target' can be
constructed by concatenating elements of the 'wordBank' array.

you may reuse elements of 'wordBank' as many times as needed.
"""

def countConstruct(target, wordBank):
    if target == "":
        return 1

    count = 0;
    for word in wordBank:
        if len(word) <= len(target):
            prefix = target[0:len(word)]
            if (prefix == word):
                count += countConstruct(target[len(word):], wordBank)
    return count

#Dynamic prgramming using memoization:
def countConstructDP(target, wordBank, table):
    if target in table:
        return table[target]
    if target == "":
        return 1

    count = 0
    for word in wordBank:
        if len(word) <= len(target):
            prefix = target[0:len(word)]
            if (prefix == word):
                sub = target[len(word):]
                count += countConstructDP(sub, wordBank, table)

    table[target] = count
    return count

print(countConstruct("abcd", ["a", "ab", "cd", "bc", "d"]))
print(countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstructDP("eeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "f"], dict()))
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "f"]))
