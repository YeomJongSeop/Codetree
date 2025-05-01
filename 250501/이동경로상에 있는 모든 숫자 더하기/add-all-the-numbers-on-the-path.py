N, T = map(int, input().split())
cmd = input()
answer = [list(map(int, input().split())) for _ in range(N)]

# Please write your code here.
#격자니까 행렬 동 남 서 북 
dxs=[0,1,0,-1]#row
dys=[1,0,-1,0]#column
s=0

# 북쪽
dir_num=3
x,y = int(N/2) , int(N/2)
s+=answer[x][y]

def in_range(x,y):
    return 0<=x and x<N and 0<=y and y<N

for a in cmd:
    if a =='R':
        dir_num= (dir_num+1)%4
    elif a =='L':
        dir_num=(dir_num-1 +4)%4
    elif a=='F':
        nx,ny= x+dxs[dir_num],y+dys[dir_num]
        if not in_range(nx,ny):
            continue
        x,y= x+dxs[dir_num],y+dys[dir_num]
        s+=answer[x][y]
    continue

print(s)



