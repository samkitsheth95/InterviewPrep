package com.Leetcode;

class missingNumber268 {

    public static int missingNumber(int[] nums) {
        int realsum = nums.length * (nums.length + 1) / 2;
        int sum = 0;
        for (int i : nums) {
            sum += i;
        }
        return realsum - sum;
    }

    public static void main(String[] args) {
        System.out.println(missingNumber(new int[]{9,6,4,2,3,5,7,0,1}));
    }
}