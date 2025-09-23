#include <iostream>
using namespace std;

int main() {
    // Please write your code here.
    char a,b;
    int ans1,ans2=0;
    cin>>a>>b;

    ans1=(int)a + (int)b;
    ans2=abs((int)a-(int)b);


    cout <<ans1<<" "<<ans2;
    return 0;
}