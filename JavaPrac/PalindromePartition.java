/*
Given a string s, partition s such that every substring of the partition is a
palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Input: s = "ccc"
Output: [["c","c","c"],["c","cc"],["cc","c"],["ccc"]]

Input: s = "bbbbb"
Output: [["b","b","b","b","b"],["b","b","b","bb"],["b","b","bb","b"],
["b","b","bbb"],["b","bb","b","b"],["b","bb","bb"],["b","bbb","b"],
["b","bbbb"],["bb","b","b","b"],["bb","b","bb"],["bb","bb","b"],["bb","bbb"],
["bbb","b","b"],["bbb","bb"],["bbbb","b"],["bbbbb"]]
 */

import java.util.List;
import java.util.ArrayList;

public class PalindromePartition {
    List<List<String>> ans = new ArrayList<>();

    public List<List<String>> partition(String s) {
        helper(new ArrayList<>(), s, -1);
        return ans;
    }

    private void helper(List<String> accu, String s, int k) {
        if (k + 1 == s.length()) {
            ans.add(accu);
            return ;
        }

        for (int i = k + 1; i < s.length(); i += 1) {
            String sub = s.substring(k + 1, i + 1);
            if (isPalindrome(sub)) {
                List<String> newAccu = new ArrayList<>(accu);
                newAccu.add(sub);
                helper(newAccu, s, i);
            }
        }

    }

    private boolean isPalindrome(String s) {
        int len = s.length() - 1;
        for (int i = 0; i < len / 1; i += 1) {
            if (s.charAt(i) != s.charAt(len - i)) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        PalindromePartition pp = new PalindromePartition();
        //be aware of the result accumulating in the filed ans.
        System.out.println(pp.partition("a"));
        System.out.println(pp.partition("bbb"));
        System.out.println(pp.partition("ccccc"));
    }

}
