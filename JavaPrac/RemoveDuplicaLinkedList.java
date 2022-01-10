/*
 Given the head of a sorted linked list, delete all nodes that have duplicate
 numbers, leaving only distinct numbers from the original list.
 Return the linked list sorted as well.


 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class RemoveDuplicaLinkedList {

    // recursive approach
    public ListNode deleteDuplicates(ListNode head) {
        if( head == null || head.next == null)
            return head;

        if(head.next.val != head.val) {
                head.next = deleteDuplicates(head.next);
        } else {
            while(head.next != null && head.val == head.next.val)
                head = head.next;
            return deleteDuplicates(head.next);
        }
        return head;
    }
    //

    /*
    public ListNode deleteDuplicates(ListNode head) {
        if(head==null || head.next==null)
            return head;

        Map<Integer,Integer> map = new LinkedHashMap<>();
        while(head!=null){
            map.put(head.val,map.getOrDefault(head.val,0)+1);
            head = head.next;
        }
        ListNode curr = new ListNode(0);
        head = curr;
        for(Map.Entry entry:map.entrySet()){
            if((int)entry.getValue()==1){
                curr.next = new ListNode((int)entry.getKey());
                curr = curr.next;
            }
        }
        return head.next;
    }
    */
}
