"""
 Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum
 and an  array of numbers as arguments.

 The function should return an array containing the shortest combination of
 numbers that add up to exactly the targetSum.

 If there is a tie for the shortest comnbination, you may return any one of
 the shortest.
 """

def bestSum(targetSum, numbers):
    if (targetSum == 0):
        return []
    if (targetSum < 0):
        return None

    result = None
    for num in numbers:
        remainder = targetSum - num
        current = bestSum(remainder, numbers)
        if (current is not None):
            current.append(num)
            if (result is None or len(current) < len(result)):
                result = current

    return result

def bestSumDP(targetSum, numbers, table):
    if targetSum in table:
        return table[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    result = None
    for num in numbers:
        remainder = targetSum - num
        current = bestSumDP(remainder, numbers, table)
        if current is not None:
            copy = []
            for element in current:
                copy.append(element)
            copy.append(num)
            if result is None or len(copy) < len(result):
                result = copy

    table[targetSum] = result
    return result


def bestSum_tabulation(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    if table[i + num] is None:
                        current = table[i]
                        way = []
                        for int in current:
                            way.append(int)
                        way.append(num)
                        table[i + num] = way
                    else:
                        current = table[i]
                        way = []
                        for int in current:
                            way.append(int)
                        way.append(num)
                        if (len(way) < len(table[i + num])):
                            table[i + num] = way

    return table[targetSum]

print(bestSum(8, [1, 4, 5]))
print(bestSumDP(100, [1, 2, 5, 25], dict()))
print(bestSum_tabulation(8, [1, 4, 5]))
print(bestSum_tabulation(100, [1, 2, 5, 25]))
print(bestSum_tabulation(80, [20, 25, 5]))
