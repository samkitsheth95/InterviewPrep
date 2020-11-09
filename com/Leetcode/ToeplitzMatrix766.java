package com.Leetcode;

public class ToeplitzMatrix766 {

    public static boolean isToeplitzMatrix(int[][] arr) {
        
        for (int i = 0; i < arr[0].length - 1; i++) {
            for (int j = 0; j < Math.min(arr.length, arr[0].length - i) - 1; j++) {
                if (arr[j][i + j] != arr[j + 1][i + j + 1]) {
                    return false;
                }
            }
        }
        
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < Math.min(arr.length - i, arr[0].length) - 1; j++) {
                if (arr[i + j][j] != arr[i + j + 1][j + 1]) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] matrix = { { 1, 2, 3, 4 }, { 5, 1, 2, 3 }, { 9, 5, 1, 2 } };
        System.out.println(isToeplitzMatrix(matrix));
    }
}