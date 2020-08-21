import java.util.*;
class concatEdgeLetters {

    private static String[] cel(String[] a) {
        String[] result = new String[a.length];        
        if(a.length == 1){ 
            return new String[]{new StringBuilder().append(a[0].charAt(0)).append(a[0].charAt(a[0].length() - 1)).toString()};
        }
        for(int i=0; i < a.length-1; i++){            
            result[i] = new StringBuilder().append(a[i].charAt(0)).append(a[i+1].charAt(a[i + 1].length() - 1)).toString();
        }
        result[a.length - 1] = new StringBuilder().append(a[a.length - 1].charAt(0)).append(a[0].charAt(a[0].length() - 1)).toString();
        return result;
    }

    public static void main(String[] args) {
        System.out.println("hello");
        String[] a = new String[] {"cat", "dog", "ferret", "scorpion"};

        for (String i : cel(a)) {
            System.out.println(i);
        }

    }
}