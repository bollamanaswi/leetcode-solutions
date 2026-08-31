bool isMonotonic(int* nums, int numsSize) {
    int increasing=true;
    int decreasing=true;
    for(int i=0;i<numsSize-1;i++){
        if(nums[i]>nums[i+1]){
            increasing=false;
        }
    }
    for(int i=0;i<numsSize-1;i++){
        if(nums[i]<nums[i+1]){
            decreasing=false;
        }
    }
    return increasing || decreasing;
}