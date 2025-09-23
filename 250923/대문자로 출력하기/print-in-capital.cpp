#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    // Please write your code here.
    string str;
    cin>>str;
    
    string ans;


    for(int i=0; i<str.length(); i++){
        if(isalpha(str[i])){
            str[i]=toupper(str[i]);
            ans+=str[i];
        }
    }

    cout<<ans;
    


    return 0;
}