"""
There are n gas stations along a circular route,
where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
from the ith station to its next (i + 1)th station. You begin the journey with
an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index
if you can travel around the circuit once in the clockwise direction,
otherwise return -1. If there exists a solution, it is guaranteed to be unique

Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""

def canCompleteCircuit_1(gas: list[int], cost: list[int]) -> int:
    extra = start= lack = 0
    for i in range(len(gas)):
        extra += gas[i] - cost[i]
        if extra < 0:
            start = i+1
            lack += extra
            extra = 0

    if extra + lack >= 0:
        return start

    return -1

# slow but passes
def canCompleteCircuit_2(gas: list[int], cost: list[int]) -> int:
    trip_tank, curr_tank, start, n = 0, 0, 0, len(gas)
    for i in range(n):
        trip_tank += gas[i] - cost[i]
        curr_tank += gas[i] - cost[i]
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
    return start if trip_tank >= 0 else -1


# vary slow: time limit exceeded
def canCompleteCircuit_3(gas: list[int], cost: list[int]) -> int:
    for i in range(len(gas)):
        if gas[i] >= cost[i]:
            if startTravel(gas, cost, i):
                return i
    return -1

def startTravel(gas, cost, idx) -> bool:
    start = idx
    tank = gas[idx] - cost[idx]
    nextIdx = idx + 1
    if nextIdx == len(gas):
        nextIdx = 0
    tank += gas[nextIdx]

    while nextIdx != start:
        if tank < cost[nextIdx]:
            return False
        tank -= cost[nextIdx]
        nextIdx += 1
        if nextIdx == len(gas):
            nextIdx = 0
        tank += gas[nextIdx]

    return True


print(canCompleteCircuit_1([1,2,3,4,5],[2,3,4,5,0]))
print(canCompleteCircuit_2([1,2,3,4,5],[2,3,4,5,0]))
print(canCompleteCircuit_3([1,2,3,4,5],[2,3,4,5,0]))

print(canCompleteCircuit_1([1,2,3,4,5,6,7],[2,3,4,5,0,4,12]))
print(canCompleteCircuit_2([1,2,3,4,5,6,7],[2,3,4,5,0,4,12]))
print(canCompleteCircuit_3([1,2,3,4,5,6,7],[2,3,4,5,0,4,12]))
