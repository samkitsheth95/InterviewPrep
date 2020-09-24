package com.Leetcode;

public class LongestIncreasingPathinaMatrix329 {

    public static int dfs(int[][] cache, int[][] matrix, int i, int j) {
        if (cache[i][j] != 0)
            return cache[i][j];
        int max = 1;
        if (i + 1 < matrix.length && matrix[i + 1][j] > matrix[i][j])
            max = Math.max(max, 1 + dfs(cache, matrix, i + 1, j));
        if (i - 1 >= 0 && matrix[i - 1][j] > matrix[i][j])
            max = Math.max(max, 1 + dfs(cache, matrix, i - 1, j));
        if (j + 1 < matrix[0].length && matrix[i][j + 1] > matrix[i][j])
            max = Math.max(max, 1 + dfs(cache, matrix, i, j + 1));
        if (j - 1 >= 0 && matrix[i][j - 1] > matrix[i][j])
            max = Math.max(max, 1 + dfs(cache, matrix, i, j - 1));
        cache[i][j] = max;
        return max;
    }

    public static int longestIncreasingPath(int[][] matrix) {
        if (matrix.length == 0)
            return 0;
        int max = 0;
        int[][] cache = new int[matrix.length][matrix[0].length];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                cache[i][j] = dfs(cache, matrix, i, j);
                max = Math.max(max, cache[i][j]);
            }
        }
        return max;
    }

    public static void main(String[] args) {
        int[][] nums = { { 9, 9, 4 }, { 6, 6, 8 }, { 2, 1, 1 } };
        System.out.println(longestIncreasingPath(nums));
    }
}
