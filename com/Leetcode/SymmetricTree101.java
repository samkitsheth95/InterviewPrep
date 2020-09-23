package com.Leetcode;

import com.DataStructure.BinarySearchTree;

public class SymmetricTree101 {

    public boolean checkSymmetric(BinarySearchTree.TreeNode left, BinarySearchTree.TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null) {
            return false;
        }
        return left.val == right.val && checkSymmetric(left.left, right.right)
                && checkSymmetric(left.right, right.left);
    }

    public boolean isSymmetric(BinarySearchTree.TreeNode root) {
        if (root == null) {
            return true;
        }
        return checkSymmetric(root.left, root.right);
    }
}
