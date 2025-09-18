#include <iostream>
#include <string>
using namespace std;

int main() {
    // Please write your code here.
    string str;

    cin>>str;

    bool exists_1 =false;
    bool exists_2 =false;

    for(int i=0; i<str.length()-1; i++){
        if (str.substr(i,2) =="ee"){
            exists_1=true;
        }
        else if(str.find("ab") !=string::npos){
            exists_2=true;
        }
    }

    if(exists_1==true) cout<<"Yes"<<" ";
    else cout<<"No"<<" ";


    if(exists_2==true) cout<<"Yes";
    else cout<<"No";
    
    return 0;
}