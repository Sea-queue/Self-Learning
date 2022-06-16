"""
A transformation sequence from word beginWord to word endWord using a dictionary
wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList.
(Note that beginWord does not need to be in wordList.)
sk == endWord

Given two words, beginWord and endWord, and a dictionary wordList,
return the number of words in the shortest transformation sequence from
beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input:
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is
"hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input:
beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList,
therefore there is no valid transformation sequence.
"""
from collections import defaultdict, deque

def wordLadder(begin: str, end: str, words: list[str]) -> int:
    if not begin or not end or not words or end not in words:
        return 0
    length = len(begin)
    all_combo = defaultdict(list)
    for w in words:
        for i in range(length):
            all_combo[w[:i] + "*" + w[i+1:]].append(w)

    queue = deque([(begin, 1)])
    visited = set()
    visited.add(begin)
    while queue:
        current_word, level = queue.popleft()
        for i in range(length):
            intermediate = current_word[:i] + "*" + current_word[i+1:]
            for w in all_combo[intermediate]:
                if w == end:
                    return level + 1
                if w not in visited:
                    visited.add(w)
                    queue.append((w, level + 1))

    return 0


print(wordLadder("hit", "cog", ["hot", "dot", "dog", "hog", "log", "cog"]))
print(wordLadder("hit", "cog", ["hot", "dot", "dog", "hog", "log"]))
