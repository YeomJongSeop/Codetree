#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.

    string str1,str2;
    int a,b;

    cin >>str1>>str2;
    
    a= stoi(str1+str2);
    b= stoi(str2+str1);

    cout<<a+b;
    return 0;
}