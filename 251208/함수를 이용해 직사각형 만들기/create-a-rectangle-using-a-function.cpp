
#include <iostream>
#include <bits/stdc++.h>

using namespace std;

void print_predict(int n,int m){
    for(int i=0; i<n; i++){
	    for(int j=0; j<m;j++){
	        cout<<"1";
	    }
	cout<<endl;
    }
}

int main() {
    int n,m;
    cin>>n>>m;
    print_predict(n,m);
    // Please write your code here.
    return 0;
}

