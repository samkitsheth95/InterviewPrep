package InterviewPrep.com.dataStructure;

import java.util.Stack;

public class BinarySearchTree{
    
    Node root;

	public void addNode(int val){
		Node newNode = new Node(val);
		Node fNode=root;

		while(true){
			if(root==null){
				root=newNode;
				break;
			}
			else if(val<=fNode.val){
				if(fNode.left==null){
					fNode.left=newNode;
					break;
				}else{
					fNode=fNode.left;
				}
			}
			else{
				if(fNode.right==null){
					fNode.right=newNode;
					break;
				}else{
					fNode=fNode.right;
				}
			}
		}
	}

	public Node getRoot(){
		return root;
	}

	public Node search(int val){
		Node fNode=root;
		while(fNode!=null && fNode.val!= val){
			if(val<fNode.val){
				fNode=fNode.left;
			}
			else{
				fNode=fNode.right;
			} 
		}

		if(fNode==null)
			return null;

	return fNode;
	}

	public void printTreeR(Node fNode){
		if(fNode!=null){
			System.out.print(fNode.val+" ");
			printTreeR(fNode.left);			
			printTreeR(fNode.right);
		}
	}

	public void printTreeI(Node fNode){
		if(fNode==null) return;
		Stack<Node> s = new Stack<Node>();
		s.push(fNode);
		while(!s.isEmpty()){
			fNode=s.pop();
			System.out.print(fNode.val +" ");			
			if(fNode.right!=null){
				s.push(fNode.right);
			}
			if(fNode.left!=null){
				s.push(fNode.left);
			}
		}
	}

	public static void main(String args[]) {
        System.out.println("Hello World!");
        BinarySearchTree newtree= new BinarySearchTree();
        newtree.addNode(10);
        newtree.addNode(15);
		newtree.addNode(19);
		newtree.addNode(17);
		newtree.addNode(11);
		newtree.printTreeI(newtree.root); // System.out.println();
		 newtree.printTreeR(newtree.root);
        // Node s=newtree.search(10);
    }

public class Node{
	public int val;
	public Node right;
	public Node left;

	public Node(int val){
		this.val=val;
	}
}
}