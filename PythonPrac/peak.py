// given a list of numbers, find the index of the peak

// [1, 3, 7, 9, 19, 23, -1, -90]

// [1,2,1] 1


def index_of_peak(nums):
	low = 0
  high = len(nums) - 1
  mid = (high + low) // 2

	while(true):
    if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
      return mid
    elif nums[mid] > nums[mid - 1]:
      low = mid
      mid = (high + low) // 2
    else
      high = mid
      mid = (high + low) // 2
