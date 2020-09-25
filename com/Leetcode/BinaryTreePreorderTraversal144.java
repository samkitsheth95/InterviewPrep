package com.Leetcode;

import java.util.List;
import java.util.ArrayList;
import java.util.Stack;

import com.DataStructure.BinarySearchTree;

public class BinaryTreePreorderTraversal144 {
    
    public static List<Integer> preorderTraversal(BinarySearchTree.TreeNode root) {
        if(root==null) return new ArrayList<Integer>();
        List<Integer> ans= new ArrayList<Integer>();
		Stack<BinarySearchTree.TreeNode> s = new Stack<BinarySearchTree.TreeNode>();
        s.push(root);
		while(!s.isEmpty()){
            BinarySearchTree.TreeNode current = s.pop();
            ans.add(current.val);
            if(current.right != null) {
                s.push(current.right);
            }
            if(current.left != null) {
                s.push(current.left);
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        BinarySearchTree newtree = new BinarySearchTree();
		newtree.addNode(3);
		newtree.addNode(20);
		newtree.addNode(9);
		newtree.addNode(15);
        newtree.addNode(7);
        for(int i : preorderTraversal(newtree.getRoot())) {
            System.out.print(i + " ");
        }
    }
}
