/* Problem - https://leetcode.com/problems/set-matrix-zeroes/ */
package com.Leetcode;

public class prob73 {

    public static void main(String[] args) {
        int a[][] = { { 0, 1, 1,1 }, { 2, 2, 2,1 }, { 3, 3, 3,1 }, { 4, 4, 4 ,0} };
        int rows = a.length;
        int columns = a[0].length;
        
        boolean[] row = new boolean[rows];
        boolean[] column = new boolean[columns];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (a[i][j] == 0) {
                   row[i]=true;
                   column[j]=true;
                }
            }
        }

        for (int i=0;i<rows;i++){
            if(row[i]){
                for(int j=0;j<columns;j++){
                    a[i][j]=0;
                }
            }
        }

        for (int i=0;i<columns;i++){
            if(column[i]){
                for(int j=0;j<rows;j++){
                    a[j][i]=0;
                }
            }
        }

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                System.out.print(a[i][j] + " ");
            }
            System.out.print("\n");
        }
    }
}