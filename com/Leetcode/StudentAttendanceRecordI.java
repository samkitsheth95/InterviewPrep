/* Problem - https://leetcode.com/problems/student-attendance-record-i/ */

package com.Leetcode;

public class StudentAttendanceRecordI {

    public static boolean checkRecord(String s) {
        int a = 0;
        char[] word = s.toCharArray();
        for (int i = 0; i < word.length; i++) {
            if (word[i] == 'A') {
                if (++a > 1) {
                    return false;
                }
            } else if (word[i] == 'L') {
                if (i + 2 < word.length && word[i + 1] == 'L' && word[i + 2] == 'L') {
                    return false;
                }
            }
        }
        return true;
    }

    public static void main(String[] args) {
        System.out.println(checkRecord("PPALLP"));
    }
}
