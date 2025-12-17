N=int(input())
li=[ list(map(int,input().split())) for _ in range(N)]
MAX_L=100
arr=[[0]*(2*MAX_L+1) for _ in range(2*MAX_L+1)]



for x,y in li:
    for i in range(x,x+8):
        for j in range(y,y+8):
            arr[i][j]=1

sum=0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        sum+=arr[i][j]

print(sum)
