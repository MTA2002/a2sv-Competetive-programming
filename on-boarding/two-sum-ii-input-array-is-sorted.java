class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int i=0;
        int j=numbers.length-1;
        int sum=0;
        while(i<=j){
            sum=numbers[i]+numbers[j];
            if(sum<target){
                i++;
            }else if(sum>target){
                j--;
            }else{
                break;
            }
        }
        int[] result={i+1,j+1};
        return result;
    }
}