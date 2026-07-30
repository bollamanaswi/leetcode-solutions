

int numberOfMatches(int n){
    int matches;
    int count=0;
    int teamsadv;
    while(n>1){
    if(n%2==0){
        matches=n/2;
        teamsadv=n/2;
        count=matches+count;
        n=teamsadv;
    }
    else{
        matches=(n-1)/2;
        teamsadv=((n-1)/2)+1;
        count=count+matches;
        n=teamsadv;
    }
    }
    return count;
}

