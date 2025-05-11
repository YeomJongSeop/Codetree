n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def is_happy(seq, m):
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            count = 1
        if count >= m:
            return True
    return False

happy = 0

# 행 검사
for row in grid:
    if is_happy(row, m):
        happy += 1

# 열 검사
for j in range(n):
    col = [grid[i][j] for i in range(n)]
    if is_happy(col, m):
        happy += 1

print(happy)