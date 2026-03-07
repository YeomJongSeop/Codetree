#include <iostream>
using namespace std;

int divider_sum(int N){
    int sum=0;
    for(int i=1; i<=N;i++){
        sum+=i;
    }
    return sum/10;

}
int main() {
    // Please write your code here.
    int N;
    cin >>N;
    cout<<divider_sum(N);


    return 0;
}