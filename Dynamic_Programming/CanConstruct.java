/*
Write a function 'canConstruct(target, wordBank)' that accepts a target string
and an array of strings.

The function should return a boolean indicating whether or not the 'target'
can be constructed by concatenating elements of the 'wordBank' array.

you may reuse elements of 'wordBank' as many times as needed.

("staketboard" ["sta", "ake", "board"]) --> false
("", ["cat", "dog"]) --> true

m = target.length()
n = wordBank.length
time: O(n^m * m)
space:  O(m^2)

memoization:
time: O(n * m^2)
space: O(m^2)
 */
import java.util.Map;
import java.util.HashMap;

public class CanConstruct {
    public boolean canConstruct(String target, String[] wordBank) {
        if (target.equals("")) return true;

        for (int i = 0; i < wordBank.length; i += 1) {
            int len = wordBank[i].length();
            if (len <= target.length()) {
                String prefix = target.substring(0, len);
                if (prefix.equals(wordBank[i])) {
                    if (canConstruct(target.substring(len), wordBank)) {
                        return true;
                    }
                }
            }
        }

        return false;
    }

    //Dynamic programming usig memoization:
    public boolean canConstruct(String target, String[] wordBank, Map<String, Boolean> table) {
        if (table.containsKey(target)) return table.get(target);
        if (target.equals("")) return true;

        for (int i = 0; i < wordBank.length; i += 1) {
            int len = wordBank[i].length();
            if (len <= target.length()) {
                String prefix = target.substring(0, len);
                if (prefix.equals(wordBank[i])) {
                    String sub = target.substring(len);
                    if (canConstruct(sub, wordBank, table)) {
                        table.put(sub, true);
                        return true;
                    }
                }
            }
        }

        table.put(target, false);
        return false;
    }

    public static void main(String[] args) {
        CanConstruct cc = new CanConstruct();
        System.out.println(cc.canConstruct("abc", new String[]{"ab", "c"}));
        System.out.println(cc.canConstruct("abcd", new String[]{"ab", "c"}));
        System.out.println(cc.canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
        new String[]{"eee", "ee", "e"}, new HashMap<String, Boolean>()));
    }
}
