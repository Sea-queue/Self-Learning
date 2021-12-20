//Implement an algorithm to determine if a string has all unique characters
public class IsUnique {

    public boolean isUniqueChars(String str) {
        if (str.length() > 128) return false;

        boolean[] charSet = new boolean[128];
        for (int i = 0; i < str.length(); i += 1) {
            int val = str.charAt(i);
            if (charSet[val]) return false;
            else charSet[val] = true;
        }
        return true;
    }

    public static void main(String[] args) {
        IsUnique obj = new IsUnique();
        String eg1 = "abcdd";
        String eg2 = "!@#$%";
        String eg3 = "";
        System.out.println(obj.isUniqueChars(eg1));
        System.out.println(obj.isUniqueChars(eg2));
        System.out.println(obj.isUniqueChars(eg3));
        System.out.println(eg1.charAt(0) - 'a');
    }
}
