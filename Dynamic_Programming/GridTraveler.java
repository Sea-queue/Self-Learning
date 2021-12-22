/*
on a 2D grid. you begin in the top-left corner and your goal is to travel to
the bottom-right corner. You may only move down or right.

In how many ways can you travel to the goal on a grid with dimensions m * n?

on a 2 x 3:

1: right, right, down
2: right, down, right
3: down, right, right

so return 3
 */

import java.util.Map;
import java.util.HashMap;

 public class GridTraveler {

     //(0, 1) --> 0
     //(1, 0) --> 0
     //(1, 1) --> 1
     public int gridTraveler(int m, int n) {
         if (m == 1 && n == 1) return 1;
         if (m == 0 || n == 0) return 0;
         return gridTraveler(m - 1, n) + gridTraveler(m, n - 1);
     }


     //Dynamic programming with memoization:
     public long gridTraveler(int m, int n, Map<String, Long> table) {
         String key = m + "," + n;
         if (table.containsKey(key)) return table.get(key);
         if (m == 0 || n == 0) return 0;
         if (m == 1 && n == 1) return 1;
         table.put(key, gridTraveler(m - 1, n, table) + gridTraveler(m, n - 1, table));
         return table.get(key);
     }


     public static void main(String[] args) {
        GridTraveler gt = new GridTraveler();
        System.out.println(gt.gridTraveler(2, 3));
        System.out.println(gt.gridTraveler(3, 2));
        System.out.println(gt.gridTraveler(18, 18, new HashMap<String, Long>()));
     }
 }
