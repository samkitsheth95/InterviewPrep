package com.Leetcode;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

import com.DataStructure.BinarySearchTree;

public class BinaryTreeLevelOrderTraversal102 {

    public static List<List<Integer>> levelOrder(BinarySearchTree.TreeNode root) {
        if (root == null) {
            return new ArrayList<>();
        }
        List<List<Integer>> ans = new ArrayList<>();
        Queue<BinarySearchTree.TreeNode> queue = new LinkedList<>();
        queue.add(root);
        int numNodes = 1;
        while (!queue.isEmpty()) {
            List<Integer> levelNums = new ArrayList<>();
            int nextLvl = 0;
            while (numNodes != 0) {
                BinarySearchTree.TreeNode current = queue.poll();
                levelNums.add(current.val);
                numNodes--;
                if (current.left != null) {
                    queue.add(current.left);
                    nextLvl++;
                }
                if (current.right != null) {
                    queue.add(current.right);
                    nextLvl++;
                }
            }
            ans.add(levelNums);
            numNodes = nextLvl;
        }
        return ans;
    }

    public static void main(String[] args) {
        BinarySearchTree newtree = new BinarySearchTree();
        newtree.addNode(3);
        newtree.addNode(2);
        newtree.addNode(20);
        newtree.addNode(9);
        newtree.addNode(15);
        newtree.addNode(7);
        for (List<Integer> level : levelOrder(newtree.getRoot())) {
            for (int levelElements : level) {
                System.out.print(levelElements + " ");
            }
            System.out.println();
        }
    }
}
