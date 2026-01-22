#include <iostream>
using namespace std;

int SUM(int N){
    int sum=0;
    for(int i=0; i<=N; i++){
        sum+=i;
    }
    return sum;
}

int main() {
    // Please write your code here.
    int N;
    cin>>N;
    cout<<(SUM(N)/10);

    return 0;
}