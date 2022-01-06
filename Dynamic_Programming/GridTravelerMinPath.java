/*
Given a m x n grid filled with non-negative numbers, find a path from top left
to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
 */

 public class GridTravelerMinPath {

     public int minPath(int[][] grid) {
         int m = grid.length;
         int n = grid[0].length;

         for (int i = 1; i < n; i += 1) {
             grid[0][i] += grid[0][i - 1];
         }
         for (int i = 1; i < m; i += 1) {
             grid[i][0] += grid[i - 1][0];
         }

         for (int i = 1; i < m; i += 1) {
             for (int j = 1; j < n; j += 1) {
                 int min = Math.min(grid[i - 1][j], grid[i][j - 1]);
                 grid[i][j] += min;
             }
         }
         return grid[m - 1][n - 1];
     }

     public static void main(String[] agrs) {
         GridTravelerMinPath gtmp = new GridTravelerMinPath();
         int[][] path1 = {
             {1,1,1},
             {1,5,5},
             {1,6,5}
         };
         int[][] path2 = {{1,3,1}};
         int[][] path3 = {{1}};

         System.out.println(gtmp.minPath(path1));
         System.out.println(gtmp.minPath(path2));
         System.out.println(gtmp.minPath(path3));
     }
 }
