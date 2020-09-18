package com.Miscellaneous;

class sumOfFirsts {

    private static int sof(int[] a) {
        int result = 0, temp = 0;
        while (true) {
            int x = -1;
            boolean found = false;
            for (int i = temp; i < a.length; i++) {
                if (a[i] != 0 || found) {
                    if (x == -1) {
                        x = a[i];
                        found = true;
                    }
                    if (a[i] - x > 0) {
                        a[i] = a[i] - x;
                    } else if (a[i] - x == 0) {
                        a[i] = 0;
                        temp = i;
                    } else {
                        break;
                    }
                }
            }
            if (x != -1)
                result += x;
            if (temp == a.length - 1)
                break;
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("hello");
        int[] a = new int[] { 4, 7, 5, 0, 0, 2, 8, 9 };
        System.out.println(sof(a));

    }
}