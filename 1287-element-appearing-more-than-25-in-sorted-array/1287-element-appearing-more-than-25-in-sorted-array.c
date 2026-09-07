int findSpecialInteger(int* arr, int arrSize) {
    int count=1;
    for(int i=0;i<arrSize-1;i++){
        if(arr[i]==arr[i+1]){
            count++;
        }
        else{
            count=1;
        }
    if (count*4>arrSize){
     return arr[i];
    }
    }
    return arr[0];

    
}