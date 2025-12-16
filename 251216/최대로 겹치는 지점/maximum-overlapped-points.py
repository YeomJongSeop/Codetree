N=int(input())
li=[list(map(int,input().split())) for _ in range(N)]
arr=[0]*100


for x,y in li:
    for i in range(x,y+1):
        arr[i]+=1

print(max(arr))