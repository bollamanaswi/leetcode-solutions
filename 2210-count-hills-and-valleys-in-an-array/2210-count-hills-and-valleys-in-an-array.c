int countHillValley(int* nums, int numsSize) {
    int hillcount=0;
    int valleycount=0;
    for(int i=1;i<numsSize-1;i++){
        if(nums[i] == nums[i-1])
        continue;

        int left=i-1;
          while(left >= 0 && nums[left] == nums[i]) {
            left--;
        }
        int right=i+1;
        while(right<numsSize && nums[right]==nums[i]){
            right++;
        }
        if(left >= 0 && right < numsSize) {
            if(nums[i] > nums[left] && nums[i] > nums[right]) {
                hillcount++;
            }
            else if(nums[i] < nums[left] && nums[i] < nums[right]) {
                valleycount++;
            }
        }
    }

    return hillcount + valleycount;
}