"""
Given an integer array nums and an integer k,
return the kth largest element in the array.

Note that it is the kth largest element in the sorted order,
not the kth distinct element.

Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
"""

import heapq

def kthLargest(nums: list[int], k: int) -> int:
    priority_queue = nums[:k]
    heapq.heapify(priority_queue)
    for num in nums[k:]:
        heapq.heappushpop(priority_queue, num)
    return priority_queue[0]

print(kthLargest([3,4,4,5,5,6], 3))
print(kthLargest([3,3,3,5,5,3], 5))
