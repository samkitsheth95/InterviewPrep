/* Problem - https://leetcode.com/problems/plus-one/ */
package com.Leetcode;

public class prob66 {
    public int[] plusOne(int[] nums) {
        for (int i=nums.length-1;i>=0;i--){
            if(nums[i]==9){
                nums[i]=0;
                if(i==0){
                    int[] xd = new int[nums.length+1];
                    xd[0]=1;
                    return xd;
                }
            }else{
                nums[i]+=1;
                break;
            }
        }
        return nums;
    }
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4 };
        System.out.print("Input ");   
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        prob66 test = new prob66();
        test.plusOne(nums);
        System.out.print("\nOutput ");
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }      
    }
}