#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    int arr[100];
    int result =0;

    for(int i=0; i<100; i++){
        cin>>arr[i];

        if (arr[i]==0){
            result = arr[i-1]+arr[i-2]+arr[i-3];
            break;
        }

    }

    cout<<result;

    return 0;
}