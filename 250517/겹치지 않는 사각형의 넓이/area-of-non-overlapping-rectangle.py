a=[ list(map(int,input().split())) for _ in range(2) ]

erase=list(map(int,input().split()))


arr=[[0]*2001 for _ in range(2001) ]

for elem in a:
    x1,y1,x2,y2 = elem[0]+1000,elem[1]+1000,elem[2]+1000,elem[3]+1000
    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[x][y]=1


x1,y1,x2,y2 = erase[0]+1000,erase[1]+1000,erase[2]+1000,erase[3]+1000
for x in range(x1,x2):
    for y in range(y1,y2):
        arr[x][y]=0

ans=0
for row in arr:
    ans+=sum(row)

print(ans)