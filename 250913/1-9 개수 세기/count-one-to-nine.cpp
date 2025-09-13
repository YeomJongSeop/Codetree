#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int count[10]={};
    int arr[10];
    int n;

    cin>>n;

    for(int i=0;i<n;i++){
        cin>>arr[i];
        count[arr[i]]++;
    }
    
    for(int i=1; i<=9; i++){
        cout<< count[i] << "\n";
    }
    
    return 0;
}