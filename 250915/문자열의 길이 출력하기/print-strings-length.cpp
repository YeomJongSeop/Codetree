#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.

    string str;
    int ans;

    for (int i=0; i<2; i++){
        cin >>str;
        ans+=str.length();
    }

    cout<< ans;


    return 0;
}