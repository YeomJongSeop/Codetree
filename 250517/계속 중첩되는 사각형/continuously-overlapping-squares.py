n=int(input())

a=[ list(map(int,input().split())) for _ in range(n)]



red=[[0]*201 for _ in range(201)]
blue=[[0]*201 for _ in range(201)]


ans=0

for i in range(len(a)):
    x1,y1,x2,y2= a[i][0]+100,a[i][1]+100,a[i][2]+100,a[i][3]+100
    if i %2 ==0: # 빨강색    
        for x in range(x1,x2):
            for y in range(y1,y2):
                red[x][y]=1
                blue[x][y]=0
    
    else: # 파랑색
        for x in range(x1,x2):
            for y in range(y1,y2):
                blue[x][y]=1
                red[x][y]=0


for row in blue:
    ans+=sum(row)

print(ans)