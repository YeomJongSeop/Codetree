n, r, c = map(int, input().split())
a = [ list(map(int, input().split())) for _ in range(n)]


x,y=r-1,c-1 # 시작점

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


# 상 하 좌 우 
dxs=[-1,1,0,0]
dys=[0,0,-1,1]

def simulate(x, y):
    dxs = [-1, 1, 0, 0]  # 상 하 좌 우
    dys = [0, 0, -1, 1]
    max_val = a[x][y]

    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and a[nx][ny] > max_val:
            return nx, ny  # 더 큰 값이 있으면 이동 좌표 반환

    return None  # 이동 불가능할 경우


path = [a[x][y]]

while True:
    result = simulate(x, y)
    if result is None:
        break  # 더 이상 이동 불가능
    x, y = result  # 새로운 위치로 이동
    path.append(a[x][y])

print(*path)


'''
def simulate():
    path=[a[x][y]]
    cur_x,cur_y=x,y

    while True:
        moved=False # 움질일지 말지 탈출 로직
        max_val=a[cur_x][cur_y]
        
        for dx,dy in zip(dxs,dys):
            nx,ny=cur_x + dx, cur_y+dy
            if in_range(nx,ny) and a[nx][ny]> max_val: #상하좌우 우선 순위니까
                cur_x,cur_y=nx,ny
                path.append(a[cur_x][cur_y])
                moved= True
                break # 우선순위때문에 나와야함 break로

        if not moved:
                break

    return path


print(*simulate()) # *쓰면 리스트 표시없이 원소만 공백으로 나옴!
'''




    






            


# Please write your code here.
