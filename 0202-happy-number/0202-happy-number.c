bool isHappy(int n) {
    while(n!=1 && n!=4){
        int sum=0;
        while(n>0){
            int remainder=n%10;
            sum=(remainder*remainder)+sum;
            n=n/10;
        }
        n=sum;
    }
    if(n==1){
        return true;
    }
    else{
        return false;
    }
}