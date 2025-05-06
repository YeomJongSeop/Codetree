n, m, t = map(int, input().split())

# Create n x n grid
a = [list(map(int, input().split())) for _ in range(n)]

# Get m marble positions
marbles = [tuple(map(int, input().split())) for _ in range(m)]
r = [pos[0]-1 for pos in marbles]
c = [pos[1]-1 for pos in marbles]

# Please write your code here.

def in_range(x,y):
    return 0<=x and x<n and  0<=y and y<n




count=[ [0]*n for _ in range(n)]




# 구슬 위치 세팅
for i in range(len(r)):
    count[r[i]][c[i]]+=1


#상하좌우 행렬
dxs=[-1,1,0,0] #행
dys=[0,0,-1,1] #열

def simulate(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    max_val = -1
    nx, ny = x, y  # 기본값은 자기 자신

    for dx, dy in zip(dxs, dys):
        tx, ty = x + dx, y + dy
        if in_range(tx, ty):
            if a[tx][ty] > max_val:
                max_val = a[tx][ty]
                nx, ny = tx, ty

    return nx, ny
            




for _ in range(t):
    next_count=[ [0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for _ in range(count[i][j]):
                nx,ny= simulate(i,j)
                next_count[nx][ny]+=1

            # 2개 이상 구슬이 모이면 터짐
    for i in range(n):
        for j in range(n):
            if next_count[i][j] > 1:
                next_count[i][j] = 0

        # count 배열 갱신
    count = next_count




ans=0
for i in range(n):
    for j in range(n):
        ans+=count[i][j]

print(ans)










