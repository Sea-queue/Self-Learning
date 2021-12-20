/*
Given an integer array nums. Each element in the array represents the maximum
jump length at that position.

Return true if you can reach the last index, or false otherwise.

Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump
length is 0, which makes it impossible to reach the last index.
 */

class Jumpable {
    public boolean canJump(int[] nums) {
        if (nums.length == 1) return true;
        boolean[] aux = new boolean[nums.length];
        aux[0] = true;

        for (int i = 0; i < nums.length; i += 1) {
            if (aux[i] == false) return false;
            for (int j = i + 1; j < Math.min(nums.length, i + nums[i] + 1); j += 1) {
                aux[j] = true;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Jumpable jump = new Jumpable();
        System.out.println(jump.canJump(new int[]{5,9,3,2,1,0,2,3,3,1,0,0}));
        System.out.println(jump.canJump(new int[]{3,2,1,0,4}));
    }
}
