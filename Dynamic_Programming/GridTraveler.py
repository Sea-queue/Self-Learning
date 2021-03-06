"""
on a 2D grid. you begin in the top-left corner and your goal is to travel to
the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

on a 2 x 3:

1: right, right, down
2: right, down, right
3: down, right, right

so return 3
"""

# recurssively solve it:
def gridTraveler_recur(m, n):
    if (m == 0 or n == 0): return 0
    if (m == 1 and n == 1): return 1
    return gridTraveler_recur(m - 1, n) + gridTraveler_recur(m, n - 1)


#Dynamic programming with memoization:
def gridTraveler(m, n, table):
    key = str(m) + "," + str(n)
    if key in table:
        return table[key]
    if (m == 0 or n == 0):
        return 0
    if (m == 1 and n == 1):
        return 1
    table[key] = gridTraveler(m - 1, n, table) + gridTraveler(m, n - 1, table)
    return table[key]


# Iteration: Tabulation:
def gridTraveler_tabulation(m, n):
    table = [[0] * (n + 1) for i in range(m + 1)]
    table[1][1] = 1

    for i in range(m + 1):
        for j in range(n + 1):
            if (i+1 <= m):
                table[i + 1][j] += table[i][j]
            if (j+1 <= n):
                table[i][j + 1] += table[i][j]

    return table[m][n]


print(gridTraveler_recur(2, 3))
print(gridTraveler_recur(5, 3))
print(gridTraveler(2, 3, dict()))
print(gridTraveler(18, 18, dict()))
print(gridTraveler_tabulation(18, 18))
