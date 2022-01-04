"""
a m x n grid.
Move either down or right at any point in time.
Trying to reach the bottom-right corner of the grid.
An obstacle and space is marked as 1 and 0 respectively in the grid.
How many unique paths would there be?
"""

def recursion(grid):
    memo = dict()
    return recursionHelp(grid, 0, 0, memo)


def recursionHelp(grid, m, n, memo):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]

    if m >= len(grid) or n >= len(grid[0]):
        return 0;

    if grid[m][n] == 1:
        return 0;

    if m == len(grid) - 1 and n == len(grid[0]) - 1 and grid[m][n] == 0:
        return 1;

    memo[key] = recursionHelp(grid, m + 1, n, memo) + recursionHelp(grid, m, n + 1, memo);
    return memo[key]


def tabulation(grid):
    m = len(grid)
    n = len(grid[0])
    table = [[0] * (n + 1) for i in range(m + 1)]
    if (grid[1][1] == 0):
        table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if i + 1 <= m and grid[i - 1][j - 1] == 0 and grid[i][j - 1] == 0:
                table[i + 1][j] += table[i][j]
            if j + 1 <= n and grid[i - 1][j - 1] == 0 and grid[i - 1][j] == 0:
                table[i][j + 1] += table[i][j]

    return table[m][n]


print(recursion([[1,0],[0,0]]))
print(recursion([[0,0,0],[0,0,0],[0,1,0],[0,0,0],[0,0,1]]))
print(recursion([[0,0,0],[0,0,0],[0,1,0],[0,0,0],[0,0,0]]))
print(recursion([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]))
print(tabulation([[1,0],[0,0]]))
print(tabulation([[0,0,0],[0,0,0],[0,1,0],[0,0,0],[0,0,1]]))
print(tabulation([[0,0,0],[0,0,0],[0,1,0],[0,0,0],[0,0,0]]))
print(tabulation([[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]))
