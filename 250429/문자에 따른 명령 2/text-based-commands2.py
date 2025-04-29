dirs = input()

x, y = 0, 0

# 동, 남, 서, 북 
dx=[1, 0, -1, 0]
dy=[0, -1, 0, 1]

dir_num = 3  # 북쪽을 바라보는 방향 

for cmd in dirs:
    if cmd == 'L':
        dir_num = (dir_num - 1) % 4  # 왼쪽으로 회전
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4  # 오른쪽으로 회전
    elif cmd == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
