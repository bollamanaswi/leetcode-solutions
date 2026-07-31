int findNumbers(int* nums, int numsSize) {
   int ans=0;
    for(int i=0;i<numsSize;i++){
        int count=0;
        int temp=nums[i];
    while(temp>0){
    count=count+1;
    temp=temp/10;
    }
if(count%2==0){
    ans++;
}
    }
return ans;
}