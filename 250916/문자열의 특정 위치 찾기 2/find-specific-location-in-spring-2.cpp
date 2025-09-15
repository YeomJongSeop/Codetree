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
        if(str_arr[i][2]== letter ||str_arr[i][3]==letter ){
            cout<<str_arr[i]<<endl;
            cnt++;
        }
    }
    

    cout<<cnt;
    return 0;
}