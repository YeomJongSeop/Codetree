#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char arr[6]={'L','E','B','R','O','S'};
    int idx = -1;
    char a;

    cin >>a;
    for(int i=0; i<6; i++){
        if(arr[i]==a){
            idx=i;
        }


    }

    if(idx== -1){
        cout<<"None";
    }
    else{
        cout<<idx;
    }

    return 0;
}