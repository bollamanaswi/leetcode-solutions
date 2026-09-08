int kthFactor(int n, int k) {
    int arr[n];
    int index=0;
    for(int i=1;i<=n;i++){
        if(n%i==0){
            arr[index]=i;
            index++;
        }
    }
    
    if(k>index){
        return -1;
    }
    return arr[k-1];
}
    
