"""
Write an efficient algorithm that searches for a value target in an
m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Input:
matrix =
[[1,4,7,11,15],
 [2,5,8,12,19],
 [3,6,9,16,22],
 [10,13,14,17,24],
 [18,21,23,26,30]],
target = 5
Output: True

target = 65
Output: False
"""

def searchMatrix_1(matrix: list[list[int]], target: int) -> bool:
    """ deploy binary search on each line """
    if not matrix or not matrix[0]:
        return False
    col_len = len(matrix[0])
    for row in matrix:
        if row[0] <= target <= row[col_len - 1]:
            left, right = 0, col_len
            while left <= right:
                idx = (left + right) // 2
                if row[idx] == target:
                    return True
                elif row[idx] < target:
                    left = idx + 1
                else:
                    right = idx - 1
    return False

def searchMatrix_2(matrix: list[list[int]], target: int) -> bool:
    """ traverce from bottom left """
    if not matrix or not matrix[0]:
        return False

    row, col = len(matrix), len(matrix[0])
    x, y = 0, row - 1  # Bottom left

    while True:
        if x >= row or y < 0:
            return False
        elif matrix[x][y] == target:
            return True
        elif matrix[x][y] < target:
            x += 1
        else:
            y -= 1



print(searchMatrix_1([], 89))
print(searchMatrix_1([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
print(searchMatrix_1([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 65))
print(searchMatrix_2([], 89))
print(searchMatrix_2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 17))
print(searchMatrix_2([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 22))
