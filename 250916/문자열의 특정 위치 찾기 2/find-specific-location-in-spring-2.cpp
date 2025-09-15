#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string str_arr[5]={"apple", "banana", "grape", "blueberry", "orange"};

    char letter;
    cin >>letter;
    int cnt=0;


    for(int i=0;i<5;i++){
        for(int j=2;j<4;j++){
            if(str_arr[i][j]== letter ){
                cout<<str_arr[i]<<endl;
                cnt++;
            }
        }
    }

    cout<<cnt;
    return 0;
}