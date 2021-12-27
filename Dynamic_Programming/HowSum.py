"""
 Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and
 an array of numbers as arguments.
 The function should return an array containing any combination of elements
 that add up to exactly the targetSum. If there is no comnbination that adds
 up to the tarrgetSum, then return null.

 If there are multiple combinations, you may return any single one.
 """

def howSum(targetSum, numbers):
    if (targetSum == 0):
        return []
    if (targetSum < 0):
        return None

    for int in numbers:
        remainder = targetSum - int
        result = howSum(remainder, numbers)
        if result is not None:
            result.append(int)
            return result

    return None


#Dynamic programming using memoization
def howSumDP(targetSum, numbers, table):
    if targetSum in table:
        return table[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        result = howSumDP(remainder, numbers, table)
        if result is not None:
            result.append(num)
            table[remainder] = result
            return result

    table[targetSum] = None
    return None


def howSum_tabulation(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    current = []
                    for int in table[i]:
                        current.append(int)
                    current.append(num)
                    table[i + num] = current

    return table[targetSum]



print(howSum(7, [3, 4]))
print(howSumDP(300, [7, 14], dict()))
print(howSum_tabulation(300, [50, 90]))
print(howSum_tabulation(21, [3, 7]))
