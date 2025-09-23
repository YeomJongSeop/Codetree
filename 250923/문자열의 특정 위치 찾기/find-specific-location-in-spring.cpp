#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string str[1];
    int idx=-1;

    for(int i=0; i<2;i++){
        cin >> str[i];
    }    

    if(str[0].find(str[1])!=string::npos){
        idx = str[0].find(str[1]);
    }

    if(idx==-1){
        cout<<"No";
    }
    else cout<<idx;


    return 0;
}