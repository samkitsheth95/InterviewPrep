class decryptStringfromAlphabettoIntegerMapping1309 {

    public static String freqAlphabets(String s) {
        char[] string = s.toCharArray();
        int j = 2;
        StringBuilder ans = new StringBuilder("");
        for (int i = 0; i < string.length; i++) {
            if (j < string.length && string[j] == '#') {
                ans.append((char) (96 + Character.getNumericValue(string[i]) * 10
                        + Character.getNumericValue(string[i + 1])));
                i = j;
                j += 3;
            } else {
                ans.append((char) (96 + Character.getNumericValue(string[i])));
                j++;
            }
        }
        return ans.toString();
    }

    public static void main(String[] args) {
        String s = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#";
        System.out.println(freqAlphabets(s));
    }
}