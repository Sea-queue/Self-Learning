
def min_cost_climing_stairs(cost):
    length = len(cost)
    table = [0] * length
    table[0] = cost[0]
    table[1] = cost[1]

    for i in range(2, length):
        table[i] = cost[i] + min(table[i - 1], table[i - 2])

    return min(table[length - 1], table[length -2])


print(min_cost_climing_stairs([2,0,1,5,2]))
print(min_cost_climing_stairs([1,100,1,1,1,100,1,1,100,1]))
