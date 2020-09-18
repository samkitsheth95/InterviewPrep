/* problem - https://leetcode.com/problems/remove-outermost-parentheses/ */
package com.Leetcode;

class prob1021{

    private static String removeOuterParentheses(String S) {  
        int temp = 0;      
        StringBuilder res = new StringBuilder();
        for(char i : S.toCharArray()){
            if (i == '(') {
                if(temp++ > 0)
                    res.append("(");                    
            } 
            else {
                if(--temp > 0)
                    res.append(")");                
            }
        }
        return res.toString();
    }

    public static void main(String[] args){
        System.out.println(removeOuterParentheses("()()"));
    }
}