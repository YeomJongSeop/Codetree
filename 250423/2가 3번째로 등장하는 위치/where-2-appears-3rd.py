import sys
input = sys.stdin.readline

N=int(input())
arr=list(map(int,input().split()))

count=0
for idx,elem in enumerate(arr):
    if elem ==2:
        count+=1
        if count==3:
            print(idx+1)

