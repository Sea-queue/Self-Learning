import java.util.List;
import java.util.ArrayList;

// This class demenstrate the similarities of
// String  --  Array  -- List
public class StrArrayList {
    public static void main(String[] args) {

        // String
        //-------
        System.out.println("String related:");

        String string = "Hello world";
        System.out.println(string.length());
        System.out.println(string.charAt(0)); //H
        System.out.println(string.charAt(2)); //first l


        // Array related:
        // --------------
        System.out.println("Array related:");
        //empty array
        int[] intArray1 = {};
        System.out.println(intArray1.length);

        int[] intArray2 = new int[]{};
        System.out.println(intArray2.length);

        int[] intArray3 = new int[0];
        System.out.println(intArray3.length);

        //non-empty array:
        int[] intArray4 = {1, 2, 3, 4, 5};
        System.out.println(intArray4.length);

        for (int i = 0; i < intArray4.length; i += 1) {
            System.out.print(intArray4[i] + " ");
        }


        // List related:
        // -------------
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

    /*
     The string s will be shuffled such that the character at the ith
     position moves to indices[i] in the shuffled string.
     */
    public String restoreString(String s, int[] indices) {
        char[] result = new char[s.length()];
        for (int i = 0; i < indices.length; i += 1) {
            result[indices[i]] = s.charAt(i);
        }
        return new String(result);
    }
}
