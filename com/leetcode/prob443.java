/* problem - https://leetcode.com/problems/string-compression/submissions/ */
class prob443 {
    public int compress(char[] chars) {
        int marker = 0, count = 1;
        for (int i = 0; i < chars.length; i++) {
            if (i < chars.length - 1 && chars[i] == chars[i + 1]) {
                count++;
            } else {
                if (count == 1) {
                    chars[marker] = chars[i];
                    marker++;
                } else {
                    if (count > 9) {
                        chars[marker] = chars[i];
                        String temp = String.valueOf(count);
                        for(int j=0;j<temp.length();j++){
                            chars[marker + 1 + j] = temp.charAt(j);
                        }
                        marker+=temp.length()+1;
                        count=1;
                    } else {
                        chars[marker] = chars[i];
                        chars[marker + 1] = (char) (count + '0');
                        marker += 2;
                        count = 1;
                    }
                }
            }
        }
        return marker;
    }

    public static void main(String[] args) {
        prob443 test = new prob443();
        char[] chars = new char[]{'a','b','c'};
        System.out.println(test.compress(chars));
        for(char c:chars){
            System.out.print(c);
        }
    }
}