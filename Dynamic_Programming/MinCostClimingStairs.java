
/*
Given an integer array cost where cost[i] is the cost of ith step on a staircase
Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.
Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.
Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.


Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
 */


public class MinCostClimingStairs {

    public int recursion(int[] cost) {
        return Math.min(recHelp(cost, 0), recHelp(cost, 1));
    }

    private int recHelp(int[] cost, int index) {
        if (index >= cost.length) {
            return 0;
        }
        return cost[index] + Math.min(recHelp(cost, index + 1), recHelp(cost, index + 2));
    }

    public int memoization(int[] cost) {
        int[] memo = new int[cost.length];
        System.out.println(memoHelp(cost, 0, memo));
        return Math.min(memoHelp(cost, 0, memo), memoHelp(cost, 1, memo));
    }

    private int memoHelp(int[] cost, int index, int[] memo) {
        if (index >= cost.length) return 0;

        if(memo[index] == 0) {
            memo[index] = Math.min(memoHelp(cost, index + 1, memo), memoHelp(cost, index + 2, memo));
        }

        return cost[index] + memo[index];
    }


    public int tabulation(int[] cost) {
        int len = cost.length;
        int[] table = new int[len];
        table[0] = cost[0];
        table[1] = cost[1];

        for (int i = 2; i < cost.length; i += 1) {
            table[i] = cost[i] + Math.min(table[i - 1], table[i - 2]);
        }

        return Math.min(table[len - 1], table[len - 2]);
    }

    public static void main(String[] args) {
        MinCostClimingStairs mccs = new MinCostClimingStairs();
        System.out.println(mccs.memoization(new int[]{10, 15, 20}));
        // System.out.println(mccs.recursion(new int[]{2,0,1,5,2}));
        // System.out.println(mccs.recursion(new int[]{1,100,1,1,1,100,1,1,100,1}));
        // System.out.println(mccs.recursion(new int[]{1,100}));
        // System.out.println(mccs.memoization(new int[]{2,0,1,5,2}));
        // System.out.println(mccs.memoization(new int[]{1,100,1,1,1,100,1,1,100,1}));
        // System.out.println(mccs.memoization(new int[]{1,100}));
        // System.out.println(mccs.tabulation(new int[]{2,0,1,5,2}));
        // System.out.println(mccs.tabulation(new int[]{1,100,1,1,1,100,1,1,100,1}));
        // System.out.println(mccs.tabulation(new int[]{1,100}));
    }
}
