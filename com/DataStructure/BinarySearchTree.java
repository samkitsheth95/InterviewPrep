package com.DataStructure;

import java.util.Stack;
import java.util.LinkedList;
import java.util.Queue;

public class BinarySearchTree {

	TreeNode root;

	public void addNode(int val) {
		TreeNode newNode = new TreeNode(val);
		TreeNode fNode = root;

		while (true) {
			if (root == null) {
				root = newNode;
				break;
			} else if (val <= fNode.val) {
				if (fNode.left == null) {
					fNode.left = newNode;
					break;
				} else {
					fNode = fNode.left;
				}
			} else {
				if (fNode.right == null) {
					fNode.right = newNode;
					break;
				} else {
					fNode = fNode.right;
				}
			}
		}
	}

	public TreeNode getRoot() {
		return root;
	}

	public TreeNode search(int val) {
		TreeNode fNode = root;
		while (fNode != null && fNode.val != val) {
			if (val < fNode.val) {
				fNode = fNode.left;
			} else {
				fNode = fNode.right;
			}
		}

		if (fNode == null)
			return null;

		return fNode;
	}

	public void printTreeR(TreeNode fNode) {
		if (fNode != null) {
			System.out.print(fNode.val + " ");
			printTreeR(fNode.left);
			printTreeR(fNode.right);
		}
	}

	public void printTreeI(TreeNode fNode) {
		if (fNode == null)
			return;
		Stack<TreeNode> s = new Stack<TreeNode>();
		s.push(fNode);
		while (!s.isEmpty()) {
			fNode = s.pop();
			System.out.print(fNode.val + " ");
			if (fNode.right != null) {
				s.push(fNode.right);
			}
			if (fNode.left != null) {
				s.push(fNode.left);
			}
		}
	}

	public void printTreeLevelOrder(TreeNode fNode) {
		if (fNode == null) {
			System.out.println("Empty Tree!");
			return;
		}
		Queue<TreeNode> queue = new LinkedList<>();
		queue.add(fNode);
		while (!queue.isEmpty()) {
			TreeNode current = queue.poll();
			System.out.print(current.val+" ");
			if (current.left != null) {
				queue.add(current.left);
			}
			if (current.right != null) {
				queue.add(current.right);
			}
		}
		System.out.println();
	}

	public static void main(String args[]) {
		System.out.println("Hello World!");
		BinarySearchTree newtree = new BinarySearchTree();
		newtree.addNode(3);
		newtree.addNode(20);
		newtree.addNode(9);
		newtree.addNode(15);
		newtree.addNode(7);
		newtree.printTreeLevelOrder(newtree.getRoot());
	}

	public class TreeNode {
		public int val;
		public TreeNode right;
		public TreeNode left;

		public TreeNode(int val) {
			this.val = val;
		}
	}
}