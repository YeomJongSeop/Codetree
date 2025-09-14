#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int n;
    cin>>n;
    int arr[100]={};
    int cnt[100]={0};

    for(int i=0;i<n;i++){
        cin >>arr[i];
        cnt[arr[i]]++;
    }

    int min =arr[0];

    for(int i=0;i<n;i++){
        if(arr[i]<min){
            min=arr[i];

        }
    }
    cout<<min<<" "<<cnt[min];

    return 0;
}