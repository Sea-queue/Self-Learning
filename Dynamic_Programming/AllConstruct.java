/*
 Write a function 'allConstruct(target, wordBank)' that accepts a target string
 and an array of strings.

 the function should return a 2D array containing all of the ways that the
 'target' can be constructed by concatenating elements of the 'wordBank' array.
 Each element of the 2D array should represent one combination that constructs
 the 'target'.

 you may resue elements of 'wordBank' as many time as needed.

 allConstruct(hello, [cat, dog, mouse]) --> []
 allConstruct("" [cat, dog, mouse]) --> [[]]

 m = target.length()
 n = wordBank.length
 for memoization:
 the time is still O(n^m) expenantial complexity for worst case
 because you need to list out all of the possible case.

 space: O(m): 
 */

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class AllConstruct {

    public List<List<String>> allConstruct(String target, String[] wordBank) {
        if (target.equals("")) {
            List<List<String>> empty = new ArrayList<>();
            empty.add(new ArrayList<String>());
            return empty;
        }

        List<List<String>> current = new ArrayList<List<String>>();
        for (int i = 0; i < wordBank.length; i += 1) {
            int len = wordBank[i].length();
            if (len <= target.length()) {
                String prefix = target.substring(0, len);
                if (prefix.equals(wordBank[i])) {
                    String sub = target.substring(len);
                    List<List<String>> ways = allConstruct(sub, wordBank);
                    for(List<String> l : ways) {
                        l.add(0, prefix);
                        current.add(l);
                    }
                }
            }
        }
        return current;
    }

    public List<List<String>> allConstruct(String target, String[] wordBank,
            Map<String, List<List<String>>> table) {
        if (table.containsKey(target)) return table.get(target);
        if (target.equals("")) {
            List<List<String>> empty = new ArrayList<>();
            empty.add(new ArrayList<String>());
            return empty;
        }

        List<List<String>> result = new ArrayList<>();
        for (int i = 0; i < wordBank.length; i += 1) {
            int len = wordBank[i].length();
            if (len <= target.length()) {
                String prefix = target.substring(0, len);
                if (prefix.equals(wordBank[i])) {
                    String sub = target.substring(len);
                    List<List<String>> ways = allConstruct(sub, wordBank, table);
                    for (List<String> l : ways) {
                        l.add(0, prefix);
                        result.add(l);
                    }
                }
            }
        }
        table.put(target, result);
        return result;
    }

    public static void main(String[] args) {
        AllConstruct ac = new AllConstruct();

        System.out.println(ac.allConstruct("abcdef",
            new String[]{"ab", "abc", "cd", "def", "abcd", "ef", "c"}));
        System.out.println(ac.allConstruct("purple",
            new String[]{"purp", "p", "ur", "le", "purpl"}));
        System.out.println(ac.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
            new String[]{"e", "ee", "eee", "eeee" }, new HashMap<String, List<List<String>>>()));
        System.out.println(ac.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
            new String[]{"e", "ee", "eee", "eeee"}));

    }
}
