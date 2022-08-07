"""
Given an integer array nums,
return true if there exists a triple of indices (i, j, k)
such that i < j < k and nums[i] < nums[j] < nums[k].
If no such indices exists, return false.

Example 1:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.

Example 2:
Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.

Example 3:
Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""
# the beauty of the ALGORITHEM
def increasingTriple(nums: list[int]) -> bool:
    first = second = float('inf')
    for num in nums:
        if num <= first:
            first = num
        elif num <= second:
            second = num
        else:
            return True
    return False


def increasingTriple_bad(nums: list[int]) -> bool:
    length = len(nums)
    if length < 3:
        return False
    visited1 = []
    visited2 = []
    visited3 = []
    l = 0
    m = 1
    r = 2
    while l < length - 2:
        while m < length - 1:
            if nums[l] < nums[m] and nums[l] not in visited1 and nums[m] not in visited2:
                while r < length:
                    if nums[m] < nums[r]:
                        return True
                    r += 1
                visited2.append(nums[m])
            m += 1
            r = m + 1
        visited1.append(nums[l])
        l += 1
        m = l + 1
        r = m + 1
    return False

print(increasingTriple([]))
print(increasingTriple([1,2]))
print(increasingTriple([1,2,1,3,2,4,3,5,2,6,1,6,7,8]))
print(increasingTriple([1,25,1,1,1,1,1,6,1,1]))

print(increasingTriple_bad([]))
print(increasingTriple_bad([1,2]))
print(increasingTriple_bad([1,2,1,3,2,4,3,5,2,6,1,6,7,8]))
print(increasingTriple_bad([1,25,1,1,1,1,1,6,1,1]))
