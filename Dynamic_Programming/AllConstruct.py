"""
 Write a function 'allConstruct(target, wordBank)' that accepts a target string
 and an array of strings.

 the function should return a 2D array containing all of the ways that the
 'target' can be constructed by concatenating elements of the 'wordBank' array.
 Each element of the 2D array should represent one combination that constructs
 the 'target'.

 you may resue elements of 'wordBank' as many time as needed.

 allConstruct(hello, [cat, dog, mouse]) --> []
 allConstruct("" [cat, dog, mouse]) --> [[]]
"""

def allConstruct(target, wordBank):
    if target == "":
        return [[]]

    result = []
    for word in wordBank:
        if len(word) <= len(target):
            prefix = target[0:len(word)]
            if (prefix == word):
                sub = target[len(word):]
                ways = allConstruct(sub, wordBank)
                for way in ways:
                    way.insert(0, prefix)
                    result.append(way)

    return result


#Dynamic programming using memoization
def allConstructDP(target, wordBank, table):
    if target in table:
        return table[target]

    if target == "":
        return [[]]

    result = []
    for word in wordBank:
        if (len(word) <= len(target)):
            prefix = target[0:len(word)]
            if (prefix == word):
                sub = target[len(word):]
                ways = allConstructDP(sub, wordBank, table)
                for way in ways:
                    way.insert(0, prefix)
                    result.append(way)

    table[target] = result
    return result


def allConstruct_tabulation(target, wordBank):
    table = [None] * (len(target) + 1)
    table[0] = [[]]

    for i in range(len(target)  + 1):
        for word in wordBank:
            if i + len(word) <= len(target):
                prefix = target[i : i + len(word)]
                if prefix == word:
                    if table[i + len(word)] is not None:
                        current = table[i]
                        for ways in current:
                            way = []
                            for str in ways:
                                way.append(str)
                            way.append(word)
                            table[i + len(word)].append(way)
                    else:
                        current = table[i]
                        copy = [] # becareful here it's not [[]]
                        for ways in current:
                            way = []
                            for str in ways:
                                way.append(str)
                            way.append(word)
                            copy.append(way)
                        table[i + len(word)] = copy

    return table[len(target)]


print(allConstruct("abcd", ["a", "ab", "abc", "c", "d"]))
print(allConstruct("hello", ["h", "he", "e", "llo", "lo", "el"]))
print(allConstructDP("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
    ["e", "ee", "eee", "eeee"], dict()))
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaaa"]))
print(allConstruct_tabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))
print(allConstruct_tabulation("hello", ["h", "he", "e", "llo", "lo", "el"]))
