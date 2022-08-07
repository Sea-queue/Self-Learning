class Solution {
     public int lengthOfLongestSubstringTwoDistinct(String s) {
         int len = Integer.MIN_VALUE;
         Map<Character, Integer> map = new HashMap<>();
         int start = 0;
         int end = 0;
         while (end < s.length()) { //O(n)
             map.put(s.charAt(end), map.getOrDefault(s.charAt(end),0) + 1);
             // System.out.println(map.size());
             // if (!map.containsKey(s.charAt(end))) {
             //     map.put(s.charAt(end), 1);
             // } else {
             //     int val = map.get(s.charAt(end));
             //     map.put(s.charAt(end), val + 1);
             // }
             if (map.size() == 2) {
                 len = Math.max(len, end - start + 1);
             }
             while (map.size() > 2) {
                 if (map.get(s.charAt(start)) <= 1) {
                     map.remove(s.charAt(start));
                 } else{
                     map.put(s.charAt(start), map.getOrDefault(s.charAt(start),0) - 1);
                 }
                 start++;
             }
             end++;
         }
         if (len == Integer.MIN_VALUE) {
             return s.length();
         }
         return len;
     }
}
