import java.util.Map;
import java.util.HashMap;

//input: 1  2  3  4  5  6  7   8
//fib:   1  1  2  3  5  8  13  21
//time: O(n^2)
//space: O(n)
public class Fibonacci {

    //Just recursive:
    public int fib(int n) {
        if (n <= 2) return 1;
        return fib(n - 1) + fib(n - 2);
    }

    //Dynamic Programming using memoization for integers:
    public int fibInt(int n, Map<Integer, Integer> fibTable) {
        if (fibTable.containsKey(n)) return fibTable.get(n);
        if (n <= 2) return 1;
        fibTable.put(n, fibInt(n - 1, fibTable) + fibInt(n - 2, fibTable));
        return fibTable.get(n);
    }

    //Dynamic programming suing memoization for Long:
    public long fibLong(int n, Map<Integer, Long> fibTable) {
        if (fibTable.containsKey(n)) return fibTable.get(n);
        if (n <= 2) return 1;
        fibTable.put(n, fibLong(n - 1, fibTable) + fibLong(n - 2, fibTable));
        return fibTable.get(n);
    }

    //Iterative: Tabulation
    //the 0th number of the sequence is 0.
    //the 1st number of the sequence is 1.
    //n:      0, 1, 2, 3, 4, 5, 6, 7,  8,  9, ...
    //fib(n): 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
    //time: O(n)  Linear
    public int fibTabulation(int n) {
        int[] table = new int[n + 3];
        table[1] = 1;
        for (int i = 0; i <= n; i += 1) {
            table[i + 1] += table[i];
            table[i + 2] += table[i];
        }
        return table[n];
    }

    //for Long number
    public long fibTabulationLong(int n) {
        long[] table = new long[n + 3];
        table[1] = 1;
        for (int i = 0; i <= n; i += 1) {
            table[i + 1] += table[i];
            table[i + 2] += table[i];
        }
        return table[n];
    }

    public static void main(String[] args) {
        Fibonacci fib = new Fibonacci();
        System.out.println(fib.fib(6));
        System.out.println(fib.fib(7));
        System.out.println(fib.fib(8));
        System.out.println(fib.fibInt(6, new HashMap<Integer, Integer>()));
        System.out.println(fib.fibInt(46, new HashMap<Integer, Integer>()));
        System.out.println(fib.fibLong(47, new HashMap<Integer, Long>()));

        System.out.println(fib.fibTabulation(8));
        System.out.println(fib.fibTabulation(46));
        System.out.println(fib.fibTabulationLong(47));
    }
}
