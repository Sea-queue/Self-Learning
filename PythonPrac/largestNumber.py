"""
Given a list of non-negative integers nums, arrange them such that they form
the largest number and return it.

Since the result may be very large, so you need to return a string instead
of an integer.

Example 1:
Input: nums = [10,2]
Output: "210"

Example 2:
Input: nums = [3,30,34,5,9]
Output: "9534330"
"""
def compare(n1, n2):
    """ true if n1 comes before n2 """
    return str(n1) + str(n2) > str(n2) + str(n1)

def largestNumber_1(nums: list[int]) -> str:
    quickSort(nums, 0, len(nums)-1)
    return str(int("".join(map(str, nums))))

def quickSort(nums, l, r):
    if l >= r:
        return
    pos = partition(nums, l, r)
    quickSort(nums, l, pos-1)
    quickSort(nums, pos+1, r)

def partition(nums, l, r):
    low = l
    while l < r:
        if compare(nums[l], nums[r]):
            nums[l], nums[low] = nums[low], nums[l]
            low += 1
        l += 1
    nums[low], nums[r] = nums[r], nums[low]
    return low

def largestNumber_2(nums: list[int]) -> str:
    # insertion sort:
    sortedList = []
    for num in nums:
        insert(sortedList, num)
    """ str(int()) again to get rid of trailing 0s """
    return str(int("".join(map(str, sortedList))))

def insert(sortedList, num) -> None:
    if not sortedList:
        sortedList.append(num)
    else:
        insert = False
        for i in range(len(sortedList)):
            if compare(num, sortedList[i]):
                sortedList.insert(i, num)
                insert = True
                break
        if not insert:
            sortedList.append(num)


print(largestNumber_1([3, 331, 30, 34, 345, 9, 6]))
print(largestNumber_2([3, 331, 30, 34, 345, 9, 6]))
