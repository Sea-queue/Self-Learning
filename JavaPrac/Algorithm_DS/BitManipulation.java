/*
Given two integers a and b:
return the sum / difference of the two integers
without using the operators + and -.

"&" AND operation, for example, 2 (0010) & 7 (0111) => 2 (0010)
"^" XOR operation, for example, 2 (0010) ^ 7 (0111) => 5 (0101)
*/

class BitManipulation {
    int sum(int a, int b) {
        if (a == 0) return b;
        if (b == 0) return a;

        while (b != 0) {
            int carry = a & b;
            a = a ^ b;
            b = carry << 1;
        }
        return a;
    }

    int sumRecur(int a, int b) {
        return (b == 0) ? a : sumRecur(a ^ b, (a & b) << 1);
    }

    // "~" NOT operation, for example, ~2(0010) => -3 (1101) (two's complement)
    // 1111 is -1, in two's complement
    // 1110 is -2, which is ~2 + 1, ~0010 => 1101, 1101 + 1 = 1110 => 2
    // 1101 is -3, which is ~3 + 1
    int negate(int a) {
        return ~a + 1;
    }

    public int subtract(int a, int b) {
    	while (b != 0) {
    		int borrow = (~a) & b;
    		a = a ^ b;
    		b = borrow << 1;
    	}
    	return a;
    }

    public int subtractRecur(int a, int b) {
	       return (b == 0) ? a : subtractRecur(a ^ b, (~a & b) << 1);
    }

    public static void main(String[] args) {
        BitManipulation bm = new BitManipulation();
        System.out.println(bm.sum(1, 3));
        System.out.println(bm.sum(-8, 3));
        System.out.println(bm.sumRecur(1, 3));
        System.out.println(bm.sumRecur(-8, 3));
        System.out.println(bm.negate(9));
        System.out.println(bm.negate(-9));
        System.out.println(bm.subtract(1, 3));
        System.out.println(bm.subtract(-8, 3));
        System.out.println(bm.subtractRecur(1, 3));
        System.out.println(bm.subtractRecur(-8, 3));
    }
}
