n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]

# Please write your code here.
answer=[ [0]*m for _ in range(n)]

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# matrix 생각
dxs=[0,1,0,-1] #row
dys=[1,0,-1,0] #column

dir_num=0 # 0동,1남2서,북3
x,y=0,0

answer[x][y]=1

for i in range(2,(n*m)+1):
    nx=x+dxs[dir_num]
    ny=y+dys[dir_num]
    if not in_range(nx,ny) or answer[nx][ny]!=0:
        dir_num = (dir_num+1)%4

    x,y= x+dxs[dir_num], y+dys[dir_num]
    answer[x][y]=i

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()

