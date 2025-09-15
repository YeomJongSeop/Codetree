#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.

    
    string str[10];
    int len=0;
    for(int i=0;i<10;i++){
        cin >>str[i];
        len += str[i].length();
    }
    cout<<len;
    
    return 0;
}