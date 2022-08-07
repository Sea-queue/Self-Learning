"""
Given a positive integer n, generate an n x n matrix filled with elements
from 1 to n2 in spiral order.

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Input: n = 1
Output: [[1]]
"""

def spiralMatrix(n:int) -> list[list[int]]:
    left, right, top, down, num = 0, n-1, 0, n-1, 1
    res = [[0 for _ in range(n)] for _ in range(n)]
    while left <= right and top <= down:
        for i in range(left, right+1):
            res[top][i] = num
            num += 1
        top += 1
        for i in range(top, down+1):
            res[i][right] = num
            num += 1
        right -= 1
        for i in range(right, left-1, -1):
            res[down][i] = num
            num += 1
        down -= 1
        for i in range(down, top-1, -1):
            res[i][left] = num
            num += 1
        left += 1
    return res

print(spiralMatrix(1))
print(spiralMatrix(3))
print(spiralMatrix(4))
