#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n,m;
    int arr[100]={0};
    int count[100]={0};

    cin >>n>>m;
    
    for(int i=0; i<=n;i++){
        cin>>arr[i];
        count[arr[i]]++;    
    }

    cout<<count[m];



    return 0;
}