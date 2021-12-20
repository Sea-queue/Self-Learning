//input: 1  2  3  4  5  6  7   8
//fib:   1  1  2  3  5  8  13  21

public class FibRecur {

    public int fib(int n) {
        if (n <= 2) return 1;
        return fib(n - 1) + fib(n - 2);
    }

    public static void main (String[] args) {
        FibRecur fib = new FibRecur();
        System.out.println(fib.fib(6));
        System.out.println(fib.fib(7));
        System.out.println(fib.fib(8));
    }
}
