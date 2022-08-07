"""
Given an n x n matrix,
where each of the rows and columns is sorted in ascending order,
return the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,
not the kth distinct element.

You must find a solution with a memory complexity better than O(n2).

Example 1:
Input: matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8
Output: 13
Explanation: The elements in the matrix are [1,5,9,10,11,12,13,13,15],
and the 8th smallest number is 13

Example 2:
Input: matrix = [[-5]], k = 1
Output: -5
"""
# completely did on solo  
import heapq
def kthSmallest(matrix: list[list[int]], k: int) -> int:
        n = len(matrix)
        accu = []
        row = 0
        col = 0
        while True:
            if row >= n:
                break
            elif row + col < k and row < n and col < n:
                heapq.heappush(accu, matrix[row][col])
                col += 1
            elif col >= n or row + col >= k:
                col = 0
                row += 1

        while k > 1:
            heapq.heappop(accu)
            k -= 1
        return heapq.heappop(accu)

print(kthSmallest([[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]],5))
print(kthSmallest([[1,5,9],[10,11,13],[12,13,15]],8))
print(kthSmallest([[-5]], 1))
