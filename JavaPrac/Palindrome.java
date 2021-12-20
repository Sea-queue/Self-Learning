/*
 Given a string, write a function to check if it is a permutation of a
 palindrome. A palindrome is word or phrase that is the same forwards and
 backwards. A permutation is a rearrangement of letters. The palindrome
 does not need to be limited to just dictionary words.

 We need to have an even number of almost all characters, so that half can
 be on one side and half can be on the other side. At most one character
 (the middle character) can have an odd count.
 */

 public class Palindrome {

     //this is case insensative:
     public static boolean isPermutationOfPalindrome_v1(String phrase) {
         int[] table = buildCharFrequencyTable(phrase);
         return checkMaxOneOdd(table);
     }

     private static int[] buildCharFrequencyTable(String phrase) {
         int[] table = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1];
         for (char c : phrase.toCharArray()) {
             int x = getCharNumber(c);
             if (x != -1) {
                 table[x] += 1;
             }
         }
         return table;
     }

     private static int getCharNumber(char c) {
         int a = Character.getNumericValue('a');
         int z = Character.getNumericValue('z');
         int val = Character.getNumericValue(c);
         if (a <= val && val <= z) {
             return val - a;
         }
         return -1;
     }

     private static boolean checkMaxOneOdd(int[] table) {
         boolean oneOdd = false;
         for (int count : table) {
             if (count % 2 == 1) {
                 oneOdd = !oneOdd;
             }
         }
         return oneOdd;
     }

     /*
      We can't optimize the big O time here since any algorithm will always
      have to look through the entire string. However, we can make some smaller
      incremental improvements. Because this is a relatively simple problem,
      it can be worthwhile to discuss some small optimizations or at least some
      tweaks.
      */
     public static boolean isPermutationOfPalindrome_v2(String phrase) {
        int countOdd = 0;
        int[] table = new int[Character.getNumericValue('z') - Character.getNumericValue('a') + 1];
        for (char c : phrase.toCharArray()) {
            int x = getCharNumber(c);
            if (x != -1) {
                table[x] += 1;
                if (table[x] % 2 == 1) {
                    countOdd += 1;
                }
                else {
                    countOdd -= 1;
                }
            }
        }
        return countOdd <= 1;
     }

     public static void main(String[] args) {
        //getNumericValue is case insensative.
        System.out.println(Character.getNumericValue('Z'));
        System.out.println(Character.getNumericValue('A'));
        System.out.println(Character.getNumericValue('z'));
        System.out.println(Character.getNumericValue('a'));
        //System.out.println(Integer.parseInt("hello"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v1("aab"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v1("aaB"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v1("aBb"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v1("aabc"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v1("aabcc"));

        System.out.println(Palindrome.isPermutationOfPalindrome_v2("aab"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v2("aaB"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v2("aBb"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v2("aabc"));
        System.out.println(Palindrome.isPermutationOfPalindrome_v2("aabcc"));
     }
 }
