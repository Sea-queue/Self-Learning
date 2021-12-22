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

    public static void main(String[] args) {
        Fibonacci fib = new Fibonacci();
        System.out.println(fib.fib(6));
        System.out.println(fib.fib(7));
        System.out.println(fib.fib(8));
        System.out.println(fib.fibInt(6, new HashMap<Integer, Integer>()));
        System.out.println(fib.fibInt(46, new HashMap<Integer, Integer>()));
        System.out.println(fib.fibLong(47, new HashMap<Integer, Long>()));
    }
}
