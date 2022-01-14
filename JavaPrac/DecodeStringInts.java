/*
A message containing letters from A-Z can be encoded into numbers using the
following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back
into letters using the reverse of the mapping above
(there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into
'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

we can decide what to do based on below options.

1: Do nothing if it is '0'
2: Decode it
3: Decode combination of i-th and (i+1)-th char if the integer version of that
combination is less than 27

Case1: Number of ways to decode at i-th char is 0
Case2: Number of ways to decode at i-th char equals to number of ways to decode at (i+1)-th char
Case3: Number of ways to decode at i-th char equals to number of ways to decode at (i+2)-th char
So If i-th char is not '0', the total number of ways to decode is the sum of Case2 and Case3

denote array cache that every i-th element is used to store number of ways to
decode the substring of s that starts from i-th character to the last

cache[i] = 0 if i-th char is 0
cache[i] = cache[i+1]
cache[i] = cache[i+2] if the integer version of the combination is less than 27

 */

 public class DecodeStringInts {
     public int solution(String s) {
         int n = s.length();
         int[] cache = new int[n + 1];
         cache[n] = 1;
         cache[n - 1] = s.charAt(n - 1) - '0' == 0 ? 0 : 1;
         for (int i = n - 2; i >= 0; i -= 1) {
           char c = s.charAt(i);
           if (c == '0') continue;
           cache[i] += cache[i + 1];
           if (c == '1' || (c == '2' && (s.charAt(i + 1) - '0' < 7))) {
             cache[i] += cache[i + 2];
           }
         }
         return cache[0];
     }

     public static void main(String[] args) {
         DecodeStringInts dsi = new DecodeStringInts();
         System.out.println(dsi.solution("012"));
         System.out.println(dsi.solution("12012"));
         System.out.println(dsi.solution("123142012"));
     }
 }
