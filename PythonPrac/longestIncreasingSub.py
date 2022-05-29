"""
Given an integer array nums, return the length of the longest strictly
increasing subsequence.

A subsequence is a sequence that can be derived from an array by deleting some
or no elements without changing the order of the remaining elements.
For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101],
therefore the length is 4.

Example 2:
Input: nums = [0,1,0,3,2,3]
Output: 4

Example 3:
Input: nums = [7,7,7,7,7,7,7]
Output: 1
"""
# Milestone: first time did it quickly from scratch with all the posibilities
# and tried with different data structures and strategies sololy.
def longestIncreasingSub(nums: list[int]) -> int:
    res = 1
    tabulation = [0] * len(nums)
    for i in range(len(nums)):
        idx = 1
        count = 0
        while i - idx >= 0:
            if nums[i] == nums[i - idx]:
                tabulation[i] = tabulation[i - idx]
                break
            elif nums[i] > nums[i - idx] and count < tabulation[i - idx]:
                count = tabulation[i - idx]
            idx += 1
        tabulation[i] = count + 1
        if tabulation[i] > res:
            res = tabulation[i]
    return res

print(longestIncreasingSub([0,1,0,3,2,3]))
print(longestIncreasingSub([10,9,2,5,3,7,101,18]))
print(longestIncreasingSub([9,9,9,9]))
