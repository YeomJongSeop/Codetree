//C++

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int make_gcd(int a, int b){
    while(b!=0){
	int remain=a%b;
	a=b;
	b=remain;    
    }
    return a;
}

int make_lcm(int a, int b){
    int gcd_val=make_gcd(a,b);

    return (a*b)/gcd_val;
}

int main(){
    int a, b;
    cin>>a>>b;    
    cout<<make_lcm(a,b);

}
