

public class Recursion {
    //Recursion on String
    public static String reverse(String input) {
        if (input.equals(""))
            return "";
        return reverse(input.substring(1)) + input.charAt(0);
    }

    //Recursion on String
    public static boolean isPalindrome(String input) {
        //base case
    	if (input.length( ) == 0 || input.length( ) == 1) return true;

        //call self on shrank input
    	if (input.charAt(0) == (input.charAt(input.length( ) - 1))) {
    		return isPalindrome(input.substring(1, input.length( ) - 1));
    	}

        //anytime if the corosponding char is not equal end the program
    	return false;
    }

    //Recursion on Number
    public static String findBinary(int input, String result) {
        //base case: when input is 0, just return the accumalator result
        if (input == 0) return result;

        //4 -> 100: 4 % 2 == 0 -> 2 % 2 == 0 -> 1 % 2 == 1
        //if not base case, update the result, in reverse order
        result = input % 2 + result;

        //shrink the input, pass in the accumulator
        return findBinary(input / 2, result);
    }

    //Sum of 1 to the given positive number
    public static int recursiveSummation(int inputNumber) {
        if (inputNumber <= 1) {
            return inputNumber;
        }
        return inputNumber + recursiveSummation(inputNumber - 1);
    }

    //Binary search on sorted list of integer return's the
    //index of the target if found, otherwise -1
    public static int binarySearch(int[] input, int target) {
        return binarySearchHelp(input, 0, input.length - 1, target);
    }

    public static int binarySearchHelp(int[] input, int left, int right, int target) {
        if(left > right) return -1;
        int mid = (left + right) / 2;
        if (input[mid] == target) return mid;
        else if (target < input[mid]) {
            return binarySearchHelp(input, left, mid - 1, target);
        }
        return binarySearchHelp(input, mid + 1, right, target);
    }


    //LinkedList reversal:
    //1 --> 2 --> 3 --> 4 --> 5 --> 6
    //when at node 6, return head 6 to the caller 5 where p gets 6
    //then update current head 5's connection
    //1 --> 2 --> 3 --> 4 --> 5 --> null
    //                        ^
    //                        |
    //                        6
    public static Node reverseList(Node head) {
        if (head == null || head.next == null) return head;
        ListNode p = reverseList(head.next);
        head.next.next = head;
        head.next = null;
        return p;
    }

    //Merge two sorted Linked Lists
    //1 --> 8 --> 22 --> 40
    //4 --> 11 --> 16 --> 20
    //As 1: ok 4 and 8, I'll point to whoever when you guys are sorted.
    public static Node sortedMerge(Node a, Node b) {
        if (a == null) return b;
        if (b == null) return a;

        if (a.data < b.data) {
            a.next = sortedMerge(a.next, b);
            return a;
        }
        else {
            b.next = sortedMerge(a, b.next);
            return b;
        }
    }

    //Insert Value into the BOTTOM of a binary search tree
    //if the data and value are equals, keep move untill reach to null.
    public Node insertNode(Node head, int data) {
        //base case is when reach to a null node(empty or none-empty tree)
        if (head == null) {
            head = new Node();
            head.value = data;
            return head;
        }
        if (head.value < data) {
            //if the data is supposed to be on the right, insert the data to
            //the right, and make head.right equals to the inserted branch.
            head.right = insertNode(head.right, data);
        }
        else {
            head.left = insertNode(head.left, data);
        }

        //each call returns the updated head, all the way back to root
        return head;
    }


    //print all Leaf Node (Depth first search)
    public static void printLeaves(Node root) {
        //base case: empty tree
        if (root == null) return;
        //base case: when reach to the end of a beanch, print
        if (root.left == null && root.right == null) {
            System.out.println(root.data + ", ");
            return;
        }

        //Keep move left until both left and right are null -- base case
        if (root.left != null) {
            printLeaves(root.left);
        }
        //after no left branch available, go one level above, and to the right
        if (root.right != null) {
            printLeaves(root.right);
        }
    }

    //Depth first search on graph
    public static boolean dfsSearch(Node node, Set<Node> visited, int goal) {
        if (node == null) return false;

        if (node.data == goal) return true;

        for (Node neighbor : node.getNeighbors()) {
            if (visitied.contains(neighbor)) continue;
            visited.add(neighbor);
            boolean isFound = dfsSearch(neighbor, visited, goal);

            //if isFound return true, otherwise continue;
            //so cannot just return isFound, it will stop right way
            if (isFound) return true;
        }

        //went through all the nodes, didn't find it.
        return false;
    }

    public static void main(String[] args) {
        System.out.println(Recursion.reverse("Seaqueue"));
        System.out.println(Recursion.isPalindrome("racecar"));
        System.out.println(Recursion.findBinary(7, ""));
        System.out.println(Recursion.recursiveSummation(4));
        int[] input = {1, 2, 3, 4, 5};
        System.out.println(Recursion.binarySearch(input, 80));
    }
}
