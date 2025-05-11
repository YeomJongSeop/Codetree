n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1]  # 0: 행(→), 1: 열(↓)
dy = [1, 0]

def is_happy_line(x, y, dir):
    cnt = 1
    prev = grid[x][y]

    max_cnt = 1  # 가장 긴 연속 구간
    for _ in range(1, n):
        x += dx[dir]
        y += dy[dir]
        if x >= n or y >= n:
            break
        if grid[x][y] == prev:
            cnt += 1
        else:
            cnt = 1
            prev = grid[x][y]
        max_cnt = max(max_cnt, cnt)

    return max_cnt >= m  # 가장 긴 연속 길이가 M 이상이면 행복

happy_count = 0

# 행
for i in range(n):
    if is_happy_line(i, 0, 0):
        happy_count += 1

# 열
for j in range(n):
    if is_happy_line(0, j, 1):
        happy_count += 1

print(happy_count)