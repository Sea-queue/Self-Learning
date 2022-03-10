import java.util.List;
import java.util.ArrayList;

// This class demenstrate the similarities of
// String  --  Array  -- List
public class StrArrayList {
    public static void main(String[] args) {

        // String
        // s.length()  |  s.charAt()
        // String.valueOf(int)  |  Integer.toString(int)
        // Character.getNumericValue(char)
        System.out.println("String related:");

        String s = "Hello World";
        System.out.println(s.length());     //11
        System.out.println(s.charAt(0));    //H
        System.out.println(s.charAt(6));    //W

        int k = 10;
        String result = String.valueOf(k);
        System.out.println("string:" + result);

        result = Integer.toString(k);
        System.out.println("string:" + result);

        char c = '3';
        k = c;
        System.out.println("c = " + k);
        k = Character.getNumericValue(c);
        System.out.println("c = " + k);


        // Array:
        // array.length
        System.out.println("Array related:");
        //empty array
        int[] arr1 = new int[0];
        System.out.println(arr1.length);

        //non-empty array:
        int[] arr2 = {1, 2, 3, 4, 5};
        System.out.println(arr2.length);

        for (int i = 0; i < arr2.length; i += 1) {
            System.out.print(arr2[i] + " ");
        }

        //2D array
        int[][] arr3 = new int[10][20];
        arr3[0][0] = 1;
        System.out.println("\narr3[0][0] = " + arr3[0][0]);

        //2D array
        int[][] arr4 = { {1, 2}, {3, 4} };
        for (int i = 0; i < 2; i++)
            for (int j = 0; j < 2; j++)
                System.out.println("arr4[" + i + "][" + j + "] = "
                                   + arr4[i][j]);


        // List related:
        // list.add("value")  |  list.remove(idx)
        // list.size()        |  list.get(ix)
        System.out.println("\n" + "List related:");

        List<Integer> intList = new ArrayList<>();
        intList.add(5);      //takes in values
        intList.add(9);
        intList.add(4);
        intList.remove(2);  //takes in index
        System.out.println(intList.size());
        System.out.println(intList.get(0));
        System.out.println(intList.get(1));
    }
}
