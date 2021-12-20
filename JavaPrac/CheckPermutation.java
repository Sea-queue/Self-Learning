/*
Given two strings, write a method to decide if one is a permutation of the
other. things to confirm with interviewer:
is it case sensitive? eg: God == dog ?
is whitespaec significant? eg: "god   " and "dog"?
*/

public class CheckPermutation {
    /*
    if two strings are permutations, then they have the same characters
    but in different order.
    Sorting the strings will put the characters from two permutations in
    the same order.
    */
    public static boolean sortVersion(String s, String t) {
        if (s.length() != t.length()) return false;
        return sort(s).equals(sort(t));
    }

    private static String sort(String s) {
        char[] content = s.toCharArray();
        java.util.Arrays.sort(content);
        return new String(content);
    }

    /*
    we can also use the definition of a permutation - two words with the
    same character counts - to implement this algorithm.
    */
    public static boolean accumulatorVersion(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] compare = new int[128];

        for (char c : s.toCharArray()) {
            compare[c] += 1;
        }

        for (char c : t.toCharArray()) {
            compare[c] -= 1;
            if (compare[c] < 0) return false;
        }
        return true;
    }


    public static void main(String[] args) {
        System.out.println(CheckPermutation.sortVersion("abs", "sba"));
        System.out.println(CheckPermutation.sortVersion("abs", "dba"));
        System.out.println(CheckPermutation.accumulatorVersion("aaa", "aba"));
        System.out.println(CheckPermutation.accumulatorVersion("abs", "dba"));
    }
}
