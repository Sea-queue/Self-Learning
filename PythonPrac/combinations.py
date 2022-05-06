
"""
Given two integers n and k, return all possible combinations of k numbers
out of the range [1, n]. you may return the answer in any order.

Input: n = 1, k = 1
Output: [[1]]

Input: n = 4, k = 2
Output:[ [2,4],[3,4],[2,3],[1,2],[1,3],[1,4]]

1 <= n <= 20
1 <= k <= n
"""

def combine_v1(n: int, k: int):
    """ slower version: Qudratic"""
    result = []
    if k == 1:
        for i in range(1, n + 1):
            result.append([i])
        return result


    else:
        result = combine_v1(n, k - 1)
        tempNewRes = []
        x = None
        for y in range(len(result)):
            atleast = max(result[y])
            for i in range(atleast + 1, n + 1):
                x = result[y][:]
                x.append(i)
                tempNewRes.append(x)
                x = None
        result = tempNewRes
        return result


def combine_v2(n: int, k: int):
    """ faster version: Log(n) """
    resultArr = list()
    arr = list()
    combine_v2_help(1, n, k, resultArr, arr)
    return resultArr


def combine_v2_help(i: int, n: int, k: int, resultArr: list[list[int]], arr: list[int]):
    if k == 0:
        res = arr.copy()
        resultArr.append(res)
        return

    if i > n:
        return

    arr.append(i)
    combine_v2_help(i + 1, n, k - 1, resultArr, arr)
    arr.pop()
    combine_v2_help(i + 1, n, k, resultArr, arr)


print(combine_v1(5, 3))
print(combine_v2(5, 3))
