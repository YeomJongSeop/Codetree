import sys
input= sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

min_val=min(arr)
count=0

for i in range(N):
    if arr[i] == min_val:
        count+=1

print(min_val,count)