"""
Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
# THIS SOLUTION IS CRAZY, THIS PROBLEM GET ME INTERESTED IN PROBLEM SOLVING
def maxProduct(nums):
    product = 1;
    result = -99999999999999999999999999999999
    for i in range(len(nums)):
        product *= nums[i]
        result = max(product, result)
        if (product == 0):
            product = 1

    product = 1

    for item in nums[::-1]:
        product *= item
        result = max(product, result)
        if product == 0:
            product = 1

    return result

print(maxProduct([2,3,0,-2,4]))
