#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string str;
    cin>>str;
    
    str =str.substr(1,str.length()) +str.substr(0,1);

    cout<<str;

    return 0;
}