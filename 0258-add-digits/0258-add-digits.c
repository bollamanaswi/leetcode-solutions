int addDigits(int num) {
    while(num>=10){
        int sum=0;
    while(num>0){
        int remainder=(num%10);
        sum=remainder+sum;
        num=num/10;
    }
    num=sum;
    }
    return num;
}
    