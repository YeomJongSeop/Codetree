#include <bits/stdc++.h>

using namespace std;

int main() {
    // Please write your code here.
    int arr[10],r1=0,r2=0,cnt=0;

    for(int i=0; i<10; i++){
        cin>>arr[i];
        if ((i+1)%2 ==0){
            r1+=arr[i];
        }
        if ((i+1)%3 ==0){
            r2+=arr[i];
            cnt++;
        }

    }




    double avg = (double)r2/cnt;


    cout << r1<<" ";
    cout <<fixed << setprecision(1) <<avg;



    return 0;
}