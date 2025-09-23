#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    int a,b;
    int c;
    string str;

    cin >>a>>b;

    c=a+b;


    str= to_string(c);
    int cnt=0;
    for(int i=0;i<str.length();i++){
        if (str[i]=='1'){
            cnt++;

        }
    }

    cout<<cnt;



    return 0;
}