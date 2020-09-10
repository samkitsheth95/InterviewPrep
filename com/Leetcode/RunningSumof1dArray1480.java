package com.Leetcode;

class RunningSumof1dArray1480 {

    public static int[] runningSum(int[] nums) {
        for (int i = 1; i < nums.length; i++) {
            nums[i] += nums[i - 1];
        }
        return nums;
    }

    public static void main(String[] args) {
        for (int i : runningSum(new int[] { 1, 2, 3, 4 })) {
            System.out.print(i + " ");
        }
    }
}