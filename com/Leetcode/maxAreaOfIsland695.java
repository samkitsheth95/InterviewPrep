package com.Leetcode;

class maxAreaofIsland695 {

    private static int findAllOne(int[][] grid, boolean[][] seen, int i, int j,int sum) {
        if (i < 0 || j<0 || i >= grid.length || j>= grid[0].length) return sum;
        if (seen[i][j]) return sum;
        seen[i][j] = true;
        if (grid[i][j] == 0){ return sum; }
        sum = sum + 1 +
        findAllOne(grid, seen, i - 1, j,sum) +
        findAllOne(grid, seen, i + 1, j,sum) +
        findAllOne(grid, seen, i, j + 1,sum) +
        findAllOne(grid, seen, i, j - 1,sum);  
        return sum;     
    }

    private static int maxAreaOfIsland(int[][] grid) {
        int sum = 0;
        boolean[][] seen = new boolean[grid.length][grid[0].length];
        
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (!seen[i][j] && grid[i][j] == 1) {
                    sum = Math.max(sum, findAllOne(grid, seen, i, j, 0));
                }
            }
        }
        return sum;
    }

    public static void main(String[] args) {
        int[][] x = new int[][] { { 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 },
                { 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0 }, { 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0 },
                { 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 },
                { 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0 }, { 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0 } };
        System.out.println(maxAreaOfIsland(x));
    }
}