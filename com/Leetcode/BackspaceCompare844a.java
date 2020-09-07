/* Problem - https://leetcode.com/problems/backspace-string-compare/ */

package com.Leetcode;

class BackspaceCompare844a {

    private static String backspaceCompareA(String S) {
        int skip = 0;
        StringBuilder s = new StringBuilder();
        for (int i = S.length() - 1; i >= 0; i--) {
            if (S.charAt(i) == '#') {
                skip++;
            } else {
                if (skip > 0) {
                    skip--;
                } else {
                    s.append(S.charAt(i));
                }
            }
        }
        return S.toString();
    }

    private static boolean backspaceCompare(String S, String T) {
        return backspaceCompareA(S).equals(backspaceCompareA(T));
    }

    public static void main(String[] args) {
        System.out.println(backspaceCompare("bxj##tw", "bxj###tw"));
    }

}