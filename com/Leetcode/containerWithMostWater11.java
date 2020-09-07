class containerWithMostWater11 {

    private static int maxAreaNaive(int[] height) {
        int carea = 0, marea = 0;
        for (int i = 0; i < height.length; i++) {
            carea = 0;
            for (int j = 0; j < height.length; j++) {
                carea = Math.min(height[i], height[j]) * (j - i);
                if (carea > marea) {
                    marea = carea;

                }
            }
        }
        return marea;
    }

    private static int maxArea(int[] height) {
        int i = 0, j = height.length - 1;
        int mArea = 0;
        // heare we are saveing one comparison of height[i] > height[j] as compared to the posted solution.
        while (i < j) {            
            if(height[i] > height[j]) {
                mArea = Math.max(mArea, height[j] * (j - i));
                j--;
            } else {
                mArea = Math.max(mArea, height[i] * (j - i));
                i++;
            }
        }
        return mArea;
    }

    public static void main(String[] args) {
        System.out.println("Hello!");
        System.out.println(maxArea(new int[] { 1, 8, 6, 2, 5, 4, 8, 3, 7 }));
    }
}