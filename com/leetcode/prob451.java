import java.util.Arrays; 

public class prob451 {

    public static void main(String[] args) {
        String s="sfeadafsdas";
        int[] arr = new int[128];
        for(int i = 0; i< s.length(); i++){
            char c = s.charAt(i);
            arr[c]++;
        }
        
        int[] sorted = Arrays.copyOf(arr, 128);
        Arrays.sort(sorted);
        
        StringBuilder sb = new StringBuilder();
        for(int i = 127; i>= 0 && sorted[i] != 0; i--){
            for(int j = 0;j< 128; j++){
                if(arr[j] == sorted[i]){
                    char c = (char) j;
                    for(int k = 0; k< arr[j]; k++){
                        sb.append(c);
                    }
                    arr[j] = 0;
                    break;
                }
            }
        }
        System.out.println(sb.toString());
    }
}

