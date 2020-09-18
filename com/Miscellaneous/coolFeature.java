package com.Miscellaneous;

import java.util.*;

class coolFeature {

    private static List<Integer> cool(int[] a, int[] b, int[][] query) {
        List<Integer> result = new ArrayList<Integer>();
        for (int[] q : query) {
            if (q[0] == 0) {
                b[q[1]] = q[2];
            } else {
                int total = 0;
                Map<Integer, Integer> sum = new HashMap<Integer, Integer>();
                for (int i = 0; i < a.length; i++) {
                    int nums = q[1] - a[i];
                    if (sum.containsKey(nums)) {
                        sum.replace(nums, sum.get(nums) + 1);
                    } else {
                        sum.put(nums, 1);
                    }
                }
                for (int i = 0; i < b.length; i++) {
                    if (sum.containsKey(b[i])) {
                        total += sum.get(b[i]);
                    }
                }
                result.add(total);
            }
        }
        return result;
    }

    public static void main(String[] args) {
        System.out.println("hello");
        int[] a = new int[] { 1, 2, 2 };
        int[] b = new int[] { 2, 3 };
        int[][] query = new int[][] { { 1, 4 }, { 0, 0, 3 }, { 1, 5 } };

        for (Integer i : cool(a, b, query)) {
            System.out.println(i);
        }

    }
}