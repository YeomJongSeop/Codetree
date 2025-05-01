n, m = map(int, input().split())

# Please write your code here.
# ord('A')와 Z로 값 찾기 # 65~90 A~Z
# print(chr(65))

def in_range(x,y):
    return 0<= x and x < n and 0<=y and y<m



answer=[[0]*m for _ in range(n)]
# matrix row column 동 남 서 북
dxs=[0,1,0,-1] # 행
dys=[1,0,-1,0] # 열

dir_num=0
x,y=0,0

cnt=65
answer[x][y]=cnt

for i in range(2,n*m+1):
    nx,ny=x+ dxs[dir_num], y+dys[dir_num]
    cnt+=1

    if not in_range(nx,ny) or answer[nx][ny]!=0:
        dir_num = (dir_num+1) % 4
    
    x,y =x+ dxs[dir_num],y+dys[dir_num]
    answer[x][y]+=cnt
    if answer[x][y] >90:
        cnt=65
        answer[x][y]=cnt


for i in range(n):
    for j in range(m):
        print(chr(answer[i][j]),end=' ')
    print()



