# coding zoom Number: 593 965 1130
def longestSub(input: str) -> int:
    """
    sliding window:
    two pinters + a dictionary
    """
    letters = dict()
    front = 0
    back = 0
    longestLen = 0

    if len(input) <= 1:
        return len(input)

    # while not the end of the string
    while front < len(input):
        frontLetter = input[front]
        front += 1
        if frontLetter in letters:
            letters[frontLetter] += 1

        elif len(letters) < 2:
            letters[frontLetter] = 1

        elif len(letters) == 2:
            # moving the back pointer forward
            while len(letters) == 2:
                backLetter = input[back]
                letters[backLetter] -= 1
                if letters[backLetter] == 0:
                    letters.pop(backLetter)
                back += 1
            letters[frontLetter] = 1

        # update the longest length if possible
        curLen = 0
        for val in letters.values():
            curLen += val
        if curLen > longestLen:
            longestLen = curLen
    return longestLen

print(longestSub("a"))
print(longestSub("aa"))
print(longestSub("acbacbdac"))
print(longestSub("abbacbba"))
print(longestSub("abbabbba"))
