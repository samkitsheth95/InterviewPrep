package com.Leetcode;

class subarrayProductLessThanK713 {
    
    private static int numSubarrayProductLessThanK(int[] nums, int k) {
        // take j and i as pointers
        int j = 0, product = 1, answer = 0;
        for(int i = 0; i < nums.length; i++){
            // if the number is greater reset product and bring j to i+1
            // this saves us lots of division if the array is very large filled with 1 or small values
            // and a middle element is greater than k.
            if(nums[i] > k){
                j = i + 1;
                product = 1;
            }
            else{
            // incerese the answer and calculate product
                answer++;
                product *= nums[i];
                while (product >= k && j <= i){
                    // divide until you find the position of j
                    product /= nums[j];
                    j++;
                }
                // add the values
                answer += i - j;                
            }
        }
        return answer;
    }

    public static void main(String[] args) {
        System.out.println(numSubarrayProductLessThanK(new int[] { 10, 5, 2, 6 }, 100));
    }
}