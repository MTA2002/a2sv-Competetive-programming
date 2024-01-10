class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int j=0;
        int sum=0;
        int minSize=100000;
        boolean set=false;
        for(int i=0;i<nums.length;i++){
            sum+=nums[i];
            while(sum>=target){
                minSize=Math.min(minSize,(i-j)+1);
                sum -= nums[j];
                j++;
                set=true;
            }
        }
        if(!set){
            minSize=0;
        }
        return minSize;
    }
}