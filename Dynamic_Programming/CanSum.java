/*
    write a function 'canSum(targetSum, numbers)' that takes in a targetSum
    and an array of numbers as arguments.
    The function should return a boolean indicating whether it is possible to
    generate the targetSum suing numbers from the array.

    You may use an element of the array as many times as needed.
    you may assume that all input numbers are nonnegative.

    canSum(7, [5, 3, 4, 7]) --> true because: 3 + 4 = 7 or 7 == 7
    canSum(7, [2, 4]) --> false
 */
import java.util.Map;
import java.util.HashMap;

public class CanSum {

    public boolean canSum(int targetSum, int[] numbers) {
        if (targetSum == 0) return true;
        if (targetSum < 0) return false;

        for (int i = 0; i < numbers.length; i += 1) {
            int remainder = targetSum - numbers[i];
            if (canSum(remainder, numbers)) return true;
        }
        return false;
    }

    //Dynamic programming using memoization:
    public boolean canSum(int targetSum, int[] numbers, Map<Integer, Boolean> table) {
        if (table.containsKey(targetSum)) return table.get(targetSum);
        if (targetSum == 0) return true;
        if (targetSum < 0) return false;

        for (int i = 0; i < numbers.length; i += 1) {
            int remainder = targetSum - numbers[i];
            table.put(remainder, canSum(remainder, numbers, table));
            if (table.get(remainder)) return true;
        }

        return false;
    }

    public boolean canSumTabulation(int targetSum, int[] numbers) {
        boolean[] table = new boolean[targetSum + 1];
        table[0] = true;

        for (int i = 0; i <= targetSum; i += 1) {
            //If I can get to current amount
            if (table[i]) {
                for (int num : numbers) {
                    if (i + num <= targetSum) {
                        table[i + num] = true;
                    }
                }
            }
        }

        return table[targetSum];
    }


    public static void main(String[] agrs) {
        CanSum cs = new CanSum();
        System.out.println(cs.canSum(7, new int[]{3, 4}));
        System.out.println(cs.canSum(7, new int[]{5, 3}));
        //System.out.println(cs.canSum(300, new int[]{7, 14}));
        System.out.println(cs.canSum(300, new int[]{7, 14}, new HashMap<Integer, Boolean>()));
        System.out.println(cs.canSumTabulation(300, new int[]{7, 14}));
        System.out.println(cs.canSumTabulation(30, new int[]{7, 14, 10}));
    }
}
