import sys
input=sys.stdin.readline

N=int(input())

arr=list(map(int,input().split()))

s=[] 
for i in range(N):
    for j in range(i+1,N):
        if arr[i]> arr[j]:
            s.append(arr[i]-arr[j])

        else:
            s.append(arr[j]-arr[i])


print(min(s))
