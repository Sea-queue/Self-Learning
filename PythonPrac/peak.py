"""
A peak element is an element that is strictly greater than its neighbors.
Given an integer array nums, find a peak element, and return its index.
If the array contains multiple peaks, return the index to any of the peaks.
"""

def index_of_peak(nums):
	if len(nums) == 1:
	        return 0
	low = 0
	high = len(nums) - 1
	mid = (high + low) // 2

	while(True):
	    if high - low == 1:
	        if nums[high] > nums[low]:
	            return high
	        else:
	            return low
	    if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
	        return mid
	    elif nums[mid] > nums[mid - 1]:
	        low = mid
	        mid = (high + low) // 2
	    else:
	        high = mid
	        mid = (high + low) // 2

print(index_of_peak([1,2,3,4,5,4,3,2,1]))
print(index_of_peak([1,2]))
print(index_of_peak([1,2,3,4,5]))
