"""
Given an array of integers heights representing the histogram's bar height
where the width of each bar is 1,
return the area of the largest rectangle in the histogram.
in any direction.
             ___
|           |   |
|        ___|   |
|       |   |   |
|       |   |   |    ___
|___    |   |   |___|   |
|   |___|   |   |   |   |
|___|___|___|___|___|___|
Input: heights = [2,1,5,7,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is in 5 and 6, which has an area = 10 units.
"""

def largestRectangle(heights: list[int]) -> int:
    stack = [-1]
    area = 0
    heights.append(0)
    for i, height in enumerate(heights):
        while heights[stack[-1]] > height:
            h = heights[stack.pop()]
            w = i - stack[-1] - 1
            area = max(area, h*w)
        stack.append(i)
    return area

print(largestRectangle([2,1,5,7,2,3])) #10
print(largestRectangle([2,1,3,4,2,3])) #8
