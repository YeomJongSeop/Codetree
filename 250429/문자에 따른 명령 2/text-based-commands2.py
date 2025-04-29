dirs = input()

x, y = 0, 0

# 북, 동, 남, 서 (시계 방향)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dir_num = 0  # 북쪽을 바라보는 방향 index

for cmd in dirs:
    if cmd == 'L':
        dir_num = (dir_num - 1) % 4  # 왼쪽으로 회전
    elif cmd == 'R':
        dir_num = (dir_num + 1) % 4  # 오른쪽으로 회전
    elif cmd == 'F':
        x += dx[dir_num]
        y += dy[dir_num]

print(x, y)
