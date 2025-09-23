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

/*
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    // 문자열을 정의합니다.
    string str;
    
    // 문자열을 입력받습니다.
    cin >> str;
    
    // 문자열의 길이를 구합니다.
    int len = str.length();
    
    // 문자를 하나하나 확인하여 알파벳일 경우 모두 대문자로 출력합니다.
    for(int i = 0; i < len; i++) {
        if((str[i] >= 'A' && str[i] <= 'Z') || (str[i] >= 'a' && str[i] <= 'z')) {
            cout << (char)toupper(str[i]);
        }
    }
    
    return 0;
}




*/