"""
You are given an integer array coins representing coins of different denominations
and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount.
If that amount of money cannot be made up by any combination of the coins,
return -1.

You may assume that you have an infinite number of each kind of coin.
Example 1:
Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1

Example 2:
Input: coins = [2], amount = 3
Output: -1

Example 3:
Input: coins = [1], amount = 0
Output: 0

Constraints:
1 <= coins.length <= 12
1 <= coins[i] <= 231 - 1
0 <= amount <= 104
"""

def coinChange(coins: list[int], amount: int) -> int:
    value1 = [0]
    value2 = []
    count = 0
    visited = [False] * (amount + 1)
    visited[0] = True

    while value1:
        count += 1
        for val in value1:
            for coin in coins:
                newVal = val + coin
                if newVal == amount:
                    return count
                elif newVal > amount:
                    continue
                elif not visited[newVal]:
                    visited[newVal] = True
                    value2.append(newVal)
        value1, value2 = value2, []
    return -1


print(coinChange([1], 9))
print(coinChange([1,2,3,5], 19))
print(coinChange([1,2,5], 11))
print(coinChange([1,19,3,2], 104))

"""
Given an integer n, return the least number of perfect square numbers that sum to n.

A perfect square is an integer that is the square of an integer; in other words,
it is the product of some integer with itself.
For example, 1, 4, 9, and 16 are perfect squares while 3 and 11 are not.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Constraints:
1 <= n <= 104
"""

# using list and pop(0) is NOT as efficient as deque,
# it makes a difference for large input
from collections import deque

def numSquares(target: int) -> int:
    """
    if would contain repeted entries, but using a list to track the visited
    entry is more expensive than just going through it again
    """
    queue = deque([(target, 0)])
    while queue:
        cur_target, count = queue.popleft()
        if cur_target**0.5 == int(cur_target**0.5):
            return count + 1
        for i in range(1, int(cur_target**0.5)+1):
            queue.append((cur_target - i*i, count + 1))

print(numSquares(19))
print(numSquares(7168))
