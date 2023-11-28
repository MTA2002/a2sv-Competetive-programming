class Solution {
    public int maxArea(int[] height) {
        int i=0;
        int j=height.length-1;
        int amount=0;
        int tempAmount;
        while(i<j){
            if(height[i]<height[j]){
                tempAmount=height[i]*(j-i);
                amount=Math.max(amount,tempAmount);
                i++;
            }else if(height[i]>height[j]){
                tempAmount=height[j]*(j-i);
                amount=Math.max(amount,tempAmount);
                j--;
            }else{
               tempAmount=height[j]*(j-i);
                amount=Math.max(amount,tempAmount);
                i++;
                j--; 
            }
        }
        return amount;
    }
}
