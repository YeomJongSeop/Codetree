n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)

# Please write your code here.
# 동 남 북 서
dxs=[0,1,-1,0] #행
dys=[1,0,0,-1] #열
    
x,y=r-1,c-1


D={'R':0,'D':1,'U':2,'L':3}

dir_num=D[d]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n



for _ in range(t):
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    if not in_range(nx, ny):  
        dir_num = 3 - dir_num
        continue

    nx,ny = x+dxs[dir_num], y+dys[dir_num]
    x,y=nx,ny


print(x+1,y+1)