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


    public List<List<String>> allConstructTabulation(String target, String[] wordBank) {
        List<List<String>>[] table = new ArrayList[target.length() + 1];
        table[0] = new ArrayList<List<String>>();
        table[0].add(new ArrayList<String>());

        for (int i = 0; i <= target.length(); i += 1) {
            for (String word : wordBank) {
                if (i + word.length() <= target.length()) {
                    String prefix = target.substring(i, i + word.length());
                    if (prefix.equals(word)) {
                        if (table[i + word.length()] != null) {
                            List<List<String>> current = table[i];
                            for (List<String> ways : current) {
                                List<String> way = new ArrayList<>();
                                for (String str : ways) {
                                    way.add(str);
                                }
                                way.add(word);
                                table[i + word.length()].add(way);
                            }
                        }
                        else {
                            List<List<String>> current = table[i];
                            List<List<String>> copy = new ArrayList<>();
                            for (List<String> ways : current) {
                                List<String> way = new ArrayList<>();
                                for (String str : ways) {
                                    way.add(str);
                                }
                                way.add(word);
                                copy.add(way);
                            }
                            table[i + word.length()] = copy;
                        }
                    }
                }
            }
        }

        return table[target.length()];
    }

    public static void main(String[] args) {
        AllConstruct ac = new AllConstruct();

        System.out.println(ac.allConstruct("abcdef",
            new String[]{"ab", "abc", "cd", "def", "abcd", "ef", "c"}));
        System.out.println(ac.allConstruct("purple",
            new String[]{"purp", "p", "ur", "le", "purpl"}));
        System.out.println(ac.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
            new String[]{"e", "ee", "eee", "eeee" }, new HashMap<String, List<List<String>>>()));
        // System.out.println(ac.allConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeef",
        //     new String[]{"e", "ee", "eee", "eeee"}));
        System.out.println(ac.allConstructTabulation("abcdef",
            new String[]{"ab", "abc", "cd", "def", "abcd", "ef", "c"}));
        System.out.println(ac.allConstructTabulation("eeeeeeeeeeef",
            new String[]{"e", "ee", "eee", "eeee"}));

        System.out.println(ac.allConstructTabulation("hello",
            new String[]{"h", "he", "e", "llo", "lo", "el"}));
    }
}
