#include <iostream>
#include <string>
using namespace std;


int main() {
    string str[1];
    int idx =-1;

    for(int i=0; i<2;i++){
        cin>>str[i];
    }

    for(int i=0; i<str[0].length(); i++){
        if(str[0][i] == str[1][0]){
            idx = i;
            break;
        }
    }
    
    if (idx==-1){
        cout<<"No";
    }
    else cout<<idx;

    return 0;

}

//아래도 정답
/*
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

*/