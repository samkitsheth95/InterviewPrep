package com.Leetcode;

class increasingDecreasingString1270 {

    private static String sortString(String s) {
        // Our hashmap for getting frequency. ASCII for a to z
        // is between 97 to 112
        int[] freq = new int[128];
        // populate our hashmap
        for (char c : s.toCharArray()) {
            freq[(int) c]++;
        }

        int temp = s.length();
        StringBuilder answer = new StringBuilder();
        // loop until all char of string are added are added
        // step 7
        while (temp > 0) {
            // go from smallest a (97) to 123(z)
            // step 1,2 and 3
            for (int i = 97; i < 123; i++) {
                if (freq[i] > 0) {
                    freq[i]--;
                    temp--;
                    answer.append((char) i);
                }
            }
            // go reverse from z to add
            // step 4, 5 and 6
            for (int i = 123; i > 96; i--) {
                if (freq[i] > 0) {
                    freq[i]--;
                    temp--;
                    answer.append((char) i);
                }
            }
        }
        return answer.toString();
    }

    public static void main(String[] args){
        System.out.println(sortString("leetcode"));
    }
}