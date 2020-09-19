package com.Leetcode;

import com.DataStructure.BinarySearchTree;

class UnivaluedBinaryTree965 {

    public static boolean areAllSame(BinarySearchTree.TreeNode root, int val) {
        if (root == null) {
            return true;
        }
        return root.val == val && areAllSame(root.left, val) && areAllSame(root.right, val);
    }

    public static boolean isUnivalTree(BinarySearchTree.TreeNode root) {
        return areAllSame(root, root.val);
    }

    public static void main(String[] args) {
        BinarySearchTree test = new BinarySearchTree();
        test.addNode(1);
        test.addNode(1);
        test.addNode(1);
        test.addNode(1);
        System.out.println(isUnivalTree(test.getRoot()));
    }
}