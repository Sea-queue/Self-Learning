"""
Given a string s and a dictionary of strings wordDict, add spaces in s
to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

the same word in the dictionary may be reused multiple times in the segmentation.
Example 1:
Input:
s = "catsanddog",
wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Example 2:
Input:
s = "pineapplepenapple",
wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog",
wordDict = ["cats","dog","sand","and","cat"]
Output: []
"""

def wordBreak(word: str, wordDict: list[str]) -> list[str]:
    return helper(word, wordDict, {})

def helper(word, wordDict, memo) -> list[str]:
    if word in memo:
        return memo[word]
    if not word:
        return {}

    res = []
    for w in wordDict:
        if not word.startswith(w):
            continue
        elif w == word:
            res.append(w)
        else:
            restCombo = helper(word[len(w):], wordDict, memo)
            for item in restCombo:
                item = w + " " + item
                res.append(item)
    memo[word] = res
    return res

print(wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak("pineapplepenapple",
["apple","pen","applepen","pine","pineapple", "pineapplepenapple"]))
