class ToeplitzMatrix {

    public static boolean isToeplitz(int[][] arr) {
        if (arr.length <= 1)
            return true;
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[0].length; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        int k = 0;
        while (k < arr.length - 1) {
            int j = 0;
            int i = arr.length - k - 2;
            while (j < k + 1) {
                if (arr[i][j] != arr[i + 1][j + 1]) {
                    return false;
                }
                i++;
                j++;
            }
            k++;
        }
        k = 0;
        while (k < arr.length - 2) {
            int j = 1 + k;
            int i = 0;
            while (j < arr.length - 2) {
                if (arr[i][j] != arr[i + 1][j + 1]) {
                    return false;
                }
                i++;
                j++;
            }
            k++;
        }
        return true;
    }

    public static void main(String[] args) {
        int[][] a = new int[][] { { 1, 2, 3, 4 }, { 5, 1, 2, 3 }, { 6, 5, 1, 2 } };
        System.out.println(isToeplitz(a));
    }
}