class prob416 {

    private static boolean canPartition(int[] nums) {
        int sum = 0;

        for (int i : nums) {
            sum += i;
        }

        if (sum % 2 != 0) {
            return false;
        }

        return subsetSumProblem(nums, sum / 2);
    }

    private static boolean subsetSumProblem(int[] a, int sum) {
        boolean[][] res = new boolean[a.length + 1][sum + 1];

        for (int i = 0; i <= a.length; i++) {
            res[i][0] = true;
        }

        for (int i = 1; i <= sum; i++) {
            res[0][i] = false;
        }

        for (int i = 1; i <= a.length; i++) {
            for (int j = 1; j <= sum; j++) {
                if (a[i - 1] <= j) {
                    res[i][j] = res[i - 1][j] || res[i - 1][j - a[i - 1]];
                } else {
                    res[i][j] = res[i - 1][j];
                }
            }
            if (res[i][sum])
                return true;
        }

        return res[a.length][sum];
    }

    public static void main(String[] args) {
        System.out.println(canPartition(new int[] { 1, 5, 11, 5 }));
    }
}