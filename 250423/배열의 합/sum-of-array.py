import sys
input=sys.stdin.readline

for _ in range(4):
    arr=list(map(int,input().split()))

    total=sum(arr)
    print(total)
