import java.util.ArrayList;
import java.util.List;
import java.util.Stack;



// a node in a tree
class Node<T> {
  T val;
  Node<T> left;
  Node<T> right;

  //constructs a Node with given values
  public Node(T val, Node<T> left, Node<T> right) {
    this.val = val;
    this.left = left;
    this.right = right;
  }

  //return the value this node contains.
  public T getVal() {
    return this.val;
  }

  //return the left node of this node
  public Node<T> getLeft() {
    return this.left;
  }

  //return the right node of this node
  public Node<T> getRight() {
    return this.right;
  }

}

//This class will use trees perform different algorithms
class TreePrac {

  //return all the value in the given tree in depthFirst order
  public static <T> List<T> depthFirstValueStack(Node<T> n) {
    if (n == null) return new ArrayList<>();

    Stack<Node<T>> tracker = new Stack<>();
    tracker.push(n);

    List<T> result = new ArrayList<>();

    while(!tracker.isEmpty()) {
      Node<T> current = tracker.pop();
      result.add(current.getVal());

      if (current.getRight() != null) tracker.push(current.getRight());
      if (current.getLeft() != null) tracker.push(current.getLeft());
    }
    return result;
  }

  //return all the value in the given tree in depthFirst order
  public static <T> List<T> depthFirstValueRecursion(Node<T> n) {
    if (n == null) return new ArrayList<>();

    List<T> left = depthFirstValueRecursion(n.getLeft()); //bde
    List<T> right = depthFirstValueRecursion(n.getRight()); //cf

    ArrayList<T> result = new ArrayList<>();
    result.add(n.getVal());
    result.addAll(left);
    result.addAll(right);
    return result;
  }

  //checks if the given tree contains the given val
  public static <T> boolean contains(Node<T> root, T target) {
    if (root == null) return false;
    if (root.getVal() == target) return true;
    return contains(root.left, target) || contains(root.right, target);
  }

  //find the minimum integer in the given tree.
  public static int findMin (Node<Integer> root) {
    if (root == null) return Integer.MAX_VALUE;
    return Math.min(root.val, Math.min(findMin(root.left), findMin(root.right)));
  }

  //entry point:
  public static void main(String[] args) {

    Node<Character> d = new Node<Character>('d', null, null);
    Node<Character>e = new Node<Character>('e', null, null);
    Node<Character>f = new Node<Character>('f', null, null);
    Node<Character>b = new Node<Character>('b', d, e);
    Node<Character>c = new Node<Character>('c', null, f);
    Node<Character>a = new Node<Character>('a', b, c);
    
    Node<Integer> n1 = new Node<Integer>(1, null, null);
    Node<Integer> n2 = new Node<Integer>(2, null, null);
    Node<Integer> n3 = new Node<Integer>(3, n1, n2);
    Node<Integer> n4 = new Node<Integer>(4, null, null);
    Node<Integer> n5 = new Node<Integer>(5, n4, null);
    Node<Integer> n6 = new Node<Integer>(6, n5, n3);
    

    System.out.println(TreePrac.depthFirstValueStack(a));
    System.out.println(TreePrac.depthFirstValueRecursion(a));
    System.out.println(TreePrac.contains(a, 'd'));
    System.out.println(TreePrac.contains(a, 'z'));
    System.out.println(TreePrac.findMin(n6));
  }
}