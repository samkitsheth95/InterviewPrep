package com.Miscellaneous;

class ToeplitzMatrix {

    public static boolean isToeplitz(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        for (int i = 0; i < arr[0].length ; i++) {
            for (int j = 0; j < Math.min(arr.length, arr[0].length - i) - 1; j++) {
                if (arr[j][i + j] != arr[j + 1][i + j + 1]) {
                    return false;
                }
            }
        }
        for (int i = 0; i < arr.length ; i++) {
            for (int j = 0; j < Math.min(arr.length - i, arr[0].length) - 1; j++) {
                if (arr[i + j][j] != arr[i + j + 1][j + 1]) {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] a = new int[][] { { 8, 8, 8, 8, 8 }, { 8, 8, 8, 8, 9 }, { 8, 8, 8, 8, 8 }, { 8, 8, 8, 8, 8 },
                { 8, 8, 8, 8, 8 } };
        System.out.println(isToeplitz(a));
    }
}