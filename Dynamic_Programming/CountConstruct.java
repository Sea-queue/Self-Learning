/*
Write a function 'countConstruct(target, wordBank)' that accepts a target string
and an array of strings

The function should return the number of ways that the 'target' can be
constructed by concatenating elements of the 'wordBank' array.

you may reuse elements of 'wordBank' as many times as needed.

m = target.length
n = wordBank.length

time and space: same with the canConstruct
 */

import java.util.Map;
import java.util.HashMap;

 public class CountConstruct {

     public int countConstruct(String target, String[] wordBank) {
         if (target.equals("")) return 1;

         int count = 0;
         for (int i = 0; i < wordBank.length; i += 1) {
             int len = wordBank[i].length();
             if (len <= target.length()) {
                 String prefix = target.substring(0, len);
                 if (prefix.equals(wordBank[i])) {
                     count += countConstruct(target.substring(len), wordBank);
                 }
             }
         }
         return count;
     }

     // Dynamic programming using memoization
     public int countConstruct(String target, String[] wordBank, Map<String, Integer> table) {
         if (table.containsKey(target)) return table.get(target);
         if (target.equals("")) return 1;

         int count = 0;
         for (int i = 0; i < wordBank.length; i += 1) {
             int len = wordBank[i].length();
             if (len <= target.length()) {
                 String prefix = target.substring(0, len);
                 if (prefix.equals(wordBank[i])) {
                     String sub = target.substring(len);
                     count += countConstruct(sub, wordBank, table);
                 }
             }
         }

         table.put(target, count);
         return count;
     }


     public static void main(String[] agrs) {
         CountConstruct cc = new CountConstruct();
         System.out.println(cc.countConstruct("abcd",
            new String[]{"a", "ab", "b", "cd", "abc", "d"}));

         System.out.println(cc.countConstruct("abcd",
            new String[]{"a", "ab", "b", "cd", "abc", "d"}));

         System.out.println(cc.countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
            new String[]{"e", "ee", "eee", "eeee", "f"}, new HashMap<String, Integer>()));

         System.out.println(cc.countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
            new String[]{"e", "ee", "eee", "eeee", "f"}));
     }
 }
