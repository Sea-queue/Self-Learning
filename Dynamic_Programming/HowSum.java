/*
 Write a function 'howSum(targetSum, numbers)' that takes in a targetSum and
 an array of numbers as arguments.
 The function should return an array containing any combination of elements
 that add up to exactly the targetSum. If there is no comnbination that adds
 up to the tarrgetSum, then return null.

 If there are multiple combinations, you may return any single one.

 howSum(7, [2, 4]) --> null
 howSum(0, [1, 3]) --> []

 brute force:
 time: O(n^m * m)
 space: O(m)

 memoization:
 time: O(n*m) n*m recurrsive calls
 space: O(m * m) m keys and each key has most m elements
 */
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class HowSum {
    public List<Integer> howSum(int targetSum, int[] numbers) {
        if (targetSum == 0) return new ArrayList<Integer>();
        if (targetSum < 0) return null;

        for (int i = 0; i < numbers.length; i += 1) {
            int remainder = targetSum  - numbers[i];
            List<Integer> result = howSum(remainder, numbers);
            if (result != null) {
                result.add(numbers[i]);
                return result;
            }
        }
        return null;
    }

    //Dynamic programming using memoization
    public List<Integer> howSum(int targetSum, int[] numbers, Map<Integer, List<Integer>> accu) {
        if (accu.containsKey(targetSum)) return accu.get(targetSum);
        if (targetSum == 0) return new ArrayList<Integer>();
        if (targetSum < 0) return null;

        for (int i = 0; i < numbers.length; i += 1) {
            int remainder = targetSum - numbers[i];
            List<Integer> result = howSum(remainder, numbers, accu);
            if (result != null) {
                result.add(numbers[i]);
                accu.put(remainder, result);
                return result;
            }
        }

        //Don't forget this case!
        accu.put(targetSum, null);
        return null;
    }


    public List<Integer> howSumTabulation(int targetSum, int[] numbers) {
        List[] table = new ArrayList[targetSum + 1];
        table[0] = new ArrayList<Integer>();

        for (int i = 0; i <= targetSum; i += 1) {
            if (table[i] != null) {
                for (int num : numbers) {
                    if (num + i <= targetSum) {
                        List<Integer> way = new ArrayList<>();
                        List<Integer> current = table[i];
                        for (Integer element : current) {
                            way.add(element);
                        }
                        way.add(num);
                        table[i + num] = way;
                    }
                }
            }
        }

        return table[targetSum];
    }

    public static void main(String[] args) {
        HowSum hs = new HowSum();

        System.out.println(hs.howSum(7, new int[]{2, 3, 4}));
        System.out.println(hs.howSum(7, new int[]{3}));
        System.out.println(hs.howSum(300, new int[]{7, 14}, new HashMap<Integer, List<Integer>>()));
        System.out.println(hs.howSumTabulation(21, new int[]{4, 7}));
    }
}
