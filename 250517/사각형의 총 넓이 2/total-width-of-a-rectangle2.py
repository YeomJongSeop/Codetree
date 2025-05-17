n=int(input())

a = [list(map(int,input().split())) for _ in range(n)]

arr=[ [0]*10 for _ in range(10)]

for elem in a:
    x1,y1,x2,y2= elem[0],elem[1],elem[2],elem[3]
    for x in range(x1,x2):
        for y in range(y1,y2):
            arr[x][y]=1

ans=0

for elem in arr:
    ans+=sum(elem)

print(ans)



