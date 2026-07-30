int maximum69Number (int num) {
   int add=0;
   int x=1;
   while(x<=num){
    int digit=(num%(x*10))/x;
    if(digit==6) add=3*x;
    x=x*10;
   }
   return num+add;
}