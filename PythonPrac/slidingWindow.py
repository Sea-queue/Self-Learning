import heapq
from collections import Counter
from heapq import heappop, heappush, heapify

"""
Given a string, return the longestSubstring length that does not
contain more than two distinct characters.
"""
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

"""
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. You can only
see the k numbers in the window. Each time the sliding window moves right by
one position.

Return the max sliding window.

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
"""

def maxSlidingWindow_1(nums: list[int], k: int) -> list[int]:
    result = []
    heap = []
    # add first k elements in the heap
    for i in range(k):
        heapq.heappush(heap, (-1*nums[i], i))
    # add the first max element in the window from heap
    result.append(-1*heap[0][0])
    for i in range(k, len(nums)):
        heapq.heappush(heap, (-1*nums[i], i))
        while heap[0][1] <= i-k:
            heapq.heappop(heap)
        result.append(-1*heap[0][0])
    return result

def maxSlidingWindow_2(nums: list[int], k: int) -> list[int]:
    ans, heap, dic = [], [-1 * i for i in nums[:k]], Counter(nums[:k])
    heapq.heapify(heap)
    ans.append(-1*heap[0])

    for i in range(k, len(nums)):
        dic[nums[i-k]] -= 1
        length = len(heap)
        while (length > 0 and dic[-1*heap[0]] == 0):
            heapq.heappop(heap)
            length -= 1
        heapq.heappush(heap, -1*nums[i])
        ans.append(-1*heap[0])
        dic[nums[i]] += 1
    return ans

print(maxSlidingWindow_1([1,3,7,-3,5,3,6,1], 3))
print(maxSlidingWindow_1([1,-1], 1))
print(maxSlidingWindow_2([1,3,7,-3,5,3,6,1], 3))
print(maxSlidingWindow_2([1,-1], 1))


"""
Given two strings s and t of lengths m and n respectively,
return the minimum window substring of s such that every character in t
(including duplicates) is included in the window.
If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.
A substring is a contiguous sequence of characters within the string.

Example 1:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.

Example 3:
Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.
"""

def minSub(s:str, t: str) -> str:
    need, missing = Counter(t), len(t)
    i = I = J = 0
    for j, c in enumerate(s, 1):
        missing -= need[c] > 0
        need[c] -= 1
        if not missing:
            while i < j and need[s[i]] < 0:
                need[s[i]] += 1
                i += 1
            if not J or J - I >= j - i:
                I, J = i, j
    return s[I:J]

print(minSub("a", "a"))
print(minSub("aa", "a"))
print(minSub("", "n"))
print(minSub("ADOBECODEBANCBA", "ABC"))
print(minSub("ADOBECODEBANCBA", "ABCA"))
