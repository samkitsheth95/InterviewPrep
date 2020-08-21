public class doublyLinkedList{
    Node head;
    Node end;

    public doublyLinkedList(){
        head=new Node();
        end=new Node();
    }

    public void addFirst(int x){
        Node newNode = new Node(x);
        if(head.next==null){
            head.next=newNode;
            end.prev=newNode;
        }
        else{
        newNode.next=head.next;
        head.next.prev=newNode;
        head.next=newNode;
        }
    }

    public int removeFirst(){
        if(head.next==null){
            return -1;
        }else{
            if(head.next.next==null){
                int temp = head.next.val;
                head.next=null;
                end.prev=null;
                return temp;
            }else{
                int temp = head.next.val;
                head.next = head.next.next;
                return temp;
            }
        }
    }

    public Node getEnd(){
        return end;
    }

    public String toString(){
        Node next = head;
        StringBuilder dbb = new StringBuilder();
        while(next.next!=null){
            dbb.append(next.val+" ");
            next=next.next;
        }
        return dbb.toString();
    }
    public static void main(String[] args){
        doublyLinkedList test = new doublyLinkedList();
        test.addFirst(10);
        test.addFirst(20);
        test.addFirst(30);
        test.addFirst(40);
        test.addFirst(50);

        System.out.println(test.toString());
        Node end = test.getEnd();

        System.out.println(end.prev.val);
    }

    class Node{
        public int val;
        public Node next;
        public Node prev;
        
        public Node(){}
        public Node(int val){
            this.val=val;
        }
    }

}