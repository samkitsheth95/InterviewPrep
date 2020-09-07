/* Problem - https://leetcode.com/problems/best-sightseeing-pair/ */
class prob1014{

    public static int maxScoreSightseeingPair(int[] A) {
        int max=0,temp=0;
        for(int i=0;i<A.length-1;i++){
            for(int j=i+1;j<A.length;j++){
                temp = A[i]+A[j]+i-j;
                if(max<temp)
                    max=temp;
            }
        }
        return max;
    }

    public static void main(String[] args){
        int[] test = {8,1,5,2,6};
        System.out.println(maxScoreSightseeingPair(test));
    }

}