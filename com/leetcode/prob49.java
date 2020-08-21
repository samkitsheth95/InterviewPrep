/* Problem - https://leetcode.com/problems/group-anagrams/ */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Arrays;

public class prob49 {    
    public static void main(String[] args) {
               
        String[] strs = new String[]{"tea","and","ace","ad","eat","dans"};
        HashMap<String,List<String>> a = new HashMap<>();

        for(String s: strs){
            char[] so = s.toCharArray();
            Arrays.sort(so);
            String sorted = String.valueOf(so);        
            if (a.get(sorted) == null) 
                    a.put(sorted, new ArrayList<String>());
            
            a.get(sorted).add(s); 
            
        }        
        List<List<String>> result = new ArrayList<>(a.values());
        // Debug
        for(int i=0;i<result.size();i++){
            System.out.print(result.get(i).size() + "#");
            for(int j=0;j<result.get(i).size();j++){
                System.out.print(result.get(i).get(j) + " ");
            }
            System.out.println();
        }

    }
}




























