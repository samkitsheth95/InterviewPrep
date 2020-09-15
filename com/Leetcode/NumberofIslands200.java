class NumberofIslands200 {

    public static void isIsland(char[][] grid, boolean[][] visited, int i, int j) {
        if (i >= grid.length || (i < 0 || j < 0) || j >= grid[0].length || visited[i][j] || grid[i][j] == '0') {
            return;
        }
        visited[i][j] = true;
        isIsland(grid, visited, i + 1, j);
        isIsland(grid, visited, i, j + 1);
        isIsland(grid, visited, i - 1, j);
        isIsland(grid, visited, i, j - 1);
    }

    public static int numIslands(char[][] grid) {
        if (grid.length == 0) {
            return 0;
        }
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int total = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (!visited[i][j] && grid[i][j] == '1') {

                    total++;
                    isIsland(grid, visited, i, j);
                }
            }
        }
        return total;
    }

    public static void main(String[] args) {
        char[][] a = { { '1', '1', '1', '1', '0' }, { '1', '1', '0', '1', '0' }, { '1', '1', '0', '0', '0' },
                { '0', '0', '0', '0', '0' } };
        System.out.println(numIslands(a));
    }
}