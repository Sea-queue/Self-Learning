/*
A valid IP address consists of exactly four integers separated by single dots.
Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses,
but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses
that can be formed by inserting dots into s. You are not allowed to reorder or
remove any digits in s. You may return the valid IP addresses in any order.
 */

import java.util.List;
import java.util.ArrayList;

 public class RestoreIPAdress {

     public List<String> restore(String ints) {
         List<String> result = new ArrayList<>();
         generate(ints, 0, "", result, 0);
         return result;
     }

     /**
      recursively generating a way to form a IP address
      s: the original string of integers
      idx: the current position on the original string of integers
      way: the possibel IP address
      result: accumulating all of the IP Address
      count: the current slot of an IP Address
      */
     private void generate(String s, int idx, String way, List<String> result, int count) {
         if (count > 4) return ;
         if (count == 4 && idx == s.length()) {
             result.add(way);
             return ;
         }

         for (int i = 1; i <= 3; i += 1) {
             if (i + idx > s.length()) return ;
             String next = s.substring(idx, idx + i);
             if (next.charAt(0) == '0' && next.length() > 1) return ; //leading 0
             if (Integer.parseInt(next) <= 255) {
                 generate(s, idx + i, way + next + (count == 3 ? "" : "."), result, count + 1);
             }
         }
     }

     public static void main(String[] agrs) {
         RestoreIPAdress rip = new RestoreIPAdress();
         System.out.println(rip.restore("1212121"));
         System.out.println(rip.restore("123"));
         System.out.println(rip.restore("1234"));
     }

 }
