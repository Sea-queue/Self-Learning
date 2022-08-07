/*
 Given a collection of numbers, nums, that might contain duplicates,
 return all possible unique permutations in any order.

 Input: nums = [1, 1, 2]
 Output: [ [1, 1, 2],
           [1, 2, 1],
           [2, 1, 1]]
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;

class ReccursivePermutation {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        //List<Integer> temp = new ArrayList();
        solve(nums, new boolean[nums.length], new ArrayList<Integer>(), result);
        return result;
    }

    private void solve(int[] nums, boolean[] set, List<Integer> temp, List<List<Integer>> result) {

        if (temp.size() == nums.length) {
            result.add(new ArrayList<Integer>(temp));
            return;
        }

        for (int i = 0; i < nums.length; i++) {
            if (set[i]) continue;
            if(i > 0 && nums[i] == nums[i-1] && !set[i-1]) continue;
            set[i] = true;
            temp.add(nums[i]);
            solve(nums, set, temp, result);
            set[i] = false;
            temp.remove(temp.size() - 1);

        }

    }

    public static void main(String[] args) {
        ReccursivePermutation rp = new ReccursivePermutation();
        List<List<Integer>> permutation = rp.permuteUnique(new int[]{1, 1, 2});

        for (List<Integer> intArray : permutation) {
            System.out.println(intArray);
        }
    }
}
