//C++

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

#define max_N 1000
int nums[max_N];

int main() {
    // Please write your code here.
    int n,k;
    cin>>n>>k;

    for(int i=0; i<n;i++){
	cin>>nums[i];
    }
    sort(nums,nums+n);
    cout<<nums[k-1];
    return 0;
}