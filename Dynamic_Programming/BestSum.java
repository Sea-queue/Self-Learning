/*
 Write a function 'bestSum(targetSum, numbers)' that takes in a targetSum
 and an  array of numbers as arguments.

 The function should return an array containing the shortest combination of
 numbers that add up to exactly the targetSum.

 If there is a tie for the shortest comnbination, you may return any one of
 the shortest.
 time: O(n^m)
 space: (m^2)
 */

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class BestSum {
    public List<Integer> bestSum(int targetSum, int[] numbers) {
        if (targetSum == 0) return new ArrayList<Integer>();
        if (targetSum < 0) return null;

        //List<Integer> result = new ArrayList<>();
        List<Integer> result = null;
        for (int i = 0; i < numbers.length; i += 1) {
             int remainder = targetSum - numbers[i];
             List<Integer> current = bestSum(remainder, numbers);
             if (current != null) {
                 current.add(numbers[i]);
                 if (result == null || current.size() < result.size()) {
                     result = current;
                 }
             }
        }

        return result;
    }

    //Dynamic programming using memoization:
    public List<Integer> bestSum(int targetSum, int[] numbers, Map<Integer, List<Integer>> table) {
        if (table.containsKey(targetSum)) return table.get(targetSum);
        if (targetSum == 0) return new ArrayList<Integer>();
        if (targetSum < 0) return null;

        List<Integer> result = null;
        for (int i = 0; i < numbers.length; i += 1) {
             int remainder = targetSum - numbers[i];
             List<Integer> current = new ArrayList<>();

             //Be careful here, Since it's not returning the imediate solution
             //Instead it returns multiple lists, I need to make a new copy for
             //each one returned, otherwise, it adds all the list to one list.
             if (bestSum(remainder, numbers, table) != null) {
                 for (Integer num : bestSum(remainder, numbers, table)) {
                     current.add(num);
                 }
                 current.add(numbers[i]);
                 if (result == null || current.size() < result.size()) {
                     result = current;
                 }
             }
        }

        table.put(targetSum, result);
        return result;
    }

    public static void main(String[] args) {
        BestSum bs = new BestSum();
        System.out.println(bs.bestSum(8, new int[]{1, 4, 5}));
        System.out.println(bs.bestSum(100, new int[]{1, 4, 5, 25}, new HashMap<Integer, List<Integer>>()));
    }
}
