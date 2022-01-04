/*
a m x n grid.
Move either down or right at any point in time.
Trying to reach the bottom-right corner of the grid.
An obstacle and space is marked as 1 and 0 respectively in the grid.
How many unique paths would there be?
*/
import java.util.Map;
import java.util.HashMap;
class GridTravelerObstacle {
    //recursion + memoization
    //returns the number of unique paths
    public int recursion(int[][] obstacleGrid) {
        Map<String, Integer> memo = new HashMap<String, Integer>();
        return pathHelp(obstacleGrid, 0, 0, memo);
    }

    private int pathHelp(int[][] obstacleGrid, int m, int n, Map<String, Integer> memo) {
        String key = m + "," + n;
        if (memo.containsKey(key)) {
            return memo.get(key);
        }
        if (m >= obstacleGrid.length || n >= obstacleGrid[0].length) {
            return 0;
        }
        if(obstacleGrid[m][n] == 1) {
            return 0;
        }
        if (m == obstacleGrid.length - 1 &&
            n == obstacleGrid[0].length - 1 &&
            obstacleGrid[m][n] == 0) {
            return 1;
        }

        memo.put(key, pathHelp(obstacleGrid, m + 1, n, memo) + pathHelp(obstacleGrid, m, n + 1, memo));
        return memo.get(key);

    }

    //tabulation
    //returns numbers of uniques path
    public int tabulation(int[][] obstacleGrid) {
        int m = obstacleGrid.length;
        int n = obstacleGrid[0].length;
        int[][] table = new int[m + 1][n + 1];
        if (obstacleGrid[0][0] != 1) table[1][1] = 1;

        for (int i = 1; i <= m; i += 1) {
            for (int j = 1; j <= n; j += 1) {
                if (i + 1 <= m
                    && obstacleGrid[i - 1][j - 1] != 1
                    && obstacleGrid[i][j - 1] != 1)
                    table[i + 1][j] += table[i][j];
                if (j + 1 <= n
                    && obstacleGrid[i - 1][j - 1] != 1
                    && obstacleGrid[i - 1][j] != 1)
                    table[i][j + 1] += table[i][j];
            }
        }

        return table[m][n];
    }

    public static void main(String[] agrs) {
        GridTravelerObstacle gto = new GridTravelerObstacle();
        int[][] grid1 = {
            {0,0,0},
            {0,0,0},
            {0,1,0},
            {0,0,0}
        };
        int[][] grid2 = {
            {0,0,0},
            {0,0,0},
            {0,1,0},
            {0,0,0},
            {0,1,1}
        };
        int[][] grid3 = {
            {1,0,0},
            {0,0,0},
        };
        System.out.println(gto.recursion(grid1));
        System.out.println(gto.recursion(grid2));
        System.out.println(gto.recursion(grid3));
        System.out.println(gto.tabulation(grid1));
        System.out.println(gto.tabulation(grid2));
        System.out.println(gto.tabulation(grid3));
    }
}
