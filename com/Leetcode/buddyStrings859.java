package com.Leetcode;

import java.util.*;

class buddyStrings859 {

    public static boolean buddyStrings(String A, String B) {
        if (A.length() != B.length()) {
            return false;
        }
        int[] freqA = new int[127];
        int[] freqB = new int[127];
        char[] a = A.toCharArray();
        char[] b = B.toCharArray();
        int sum = 0;
        boolean flag = false;
        for (int i = 0; i < a.length; i++) {
            if (a[i] != b[i]) {
                sum += 1;
            }
            if (sum > 2) {
                return false;
            }
            freqA[(int) a[i]] += 1;
            freqB[(int) b[i]] += 1;
        }
        int temp = 0;
        for (int i = 97; i < 123; i++) {
            temp += freqA[i] * i - freqB[i] * i;
            if ((freqA[i] == freqB[i]) && freqA[i] >= 2) {
                flag = true;
            }
        }
        if (temp == 0 && flag) {
            return true;
        }
        if (sum != 2 || temp != 0) {
            return false;
        }
        return true;
    }

    public static boolean buddyStringsBetter(String A, String B) {

        int A_length = A.length();
        char Achar[] = A.toCharArray();

        if (A_length != B.length())
            return false;

        if (A.equals(B)) {
            Set set1 = new HashSet();
            for (int i = 0; i < A_length; i++) {
                if (set1.contains(Achar[i]))
                    return true;
                else
                    set1.add(Achar[i]);
            }
            return false;
        }

        char Bchar[] = B.toCharArray();
        char A1 = 0, B1 = 0; // when the 1st Discrepancy happen,A1 is Achar[i], B1 is Bchar[i]
        int j = 0; // j :count the number of Achar[i]!=Bchar[i]
        for (int i = 0; i < A_length && j < 3; i++) {
            if (Achar[i] != Bchar[i]) {
                j++;
                if (j == 1) {
                    A1 = Achar[i]; // record Achar[i] and Bchar[i] in A1, B1.
                    B1 = Bchar[i];
                }
                if (j == 2 && (Achar[i] != B1 || Bchar[i] != A1)) // when the 2st Discrepancy happen :
                                                                  // the only false situation here when j==2
                    return false;

            }
        }
        return j == 2; // the rest situation:
                       // all the other j==2 situation is true after loop,
                       // j=1 false, because unable to swap.
                       // j>2 false, because we can swap only 2 letters.
    }

    public static void main(String[] args) {
        System.out.println(buddyStringsBetter("ab", "ba"));
    }
}