/* Problem - https://leetcode.com/problems/product-of-array-except-self/ */

public class prob238 {
    public static void main(String[] args) {
        int[] nums = { 1, 2, 3, 4 };
        int[] arr = new int[nums.length];
        arr[0] = 1;
        arr[1] = nums[0];
        for (int i = 1; i < nums.length - 1; i++) {
            arr[i + 1] = nums[i] * arr[i];
        }
        int temp = 1;
        for (int i = nums.length - 2; i >= 0; i--) {

            temp = nums[i + 1] * temp;
            arr[i] = temp * arr[i];
        }   
        // Debug Code
        System.out.print("Input ");   
        for (int i = 0; i < nums.length; i++) {
            System.out.print(nums[i] + " ");
        }
        System.out.print("\nOutput ");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }      
    }
}