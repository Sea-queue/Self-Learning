"""
write a function 'canSum(targetSum, numbers)' that takes in a targetSum
and an array of numbers as arguments.
The function should return a boolean indicating whether it is possible to
generate the targetSum suing numbers from the array.

You may use an element of the array as many times as needed.
you may assume that all input numbers are nonnegative.
"""

def canSum(n, intList):
    if (n == 0):
        return True
    if (n < 0):
        return False

    for int in intList:
        remainder = n - int
        if (canSum(remainder, intList)):
            return True

    return False;


# Dynamic programming using memoization:
def canSumDP(n, intList, table):
    if n in table:
        return table[n]
    if (n == 0):
        return True
    if (n < 0):
        return False

    for int in intList:
        remainder = n - int
        table[remainder] = canSumDP(remainder, intList, table)
        if (table[remainder]):
            return True

    return False


print(canSum(7, [3, 4]))
print(canSum(7, [5, 3]))
# print(canSum(300, [7, 14]))
print(canSumDP(300, [7, 14], dict()))
