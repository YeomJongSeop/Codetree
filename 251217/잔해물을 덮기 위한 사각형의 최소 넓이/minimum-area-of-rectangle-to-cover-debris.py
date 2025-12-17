MAX_K = 1000
OFF = MAX_K
N = 2 * MAX_K + 1

arr = [[0] * N for _ in range(N)]

a1, b1, c1, d1 = map(int, input().split())
a2, b2, c2, d2 = map(int, input().split())

# 1번: 칠하기
for i in range(a1, c1):
    for j in range(b1, d1):
        arr[i + OFF][j + OFF] = 1

# 2번: 덮기(지우기)
for i in range(a2, c2):
    for j in range(b2, d2):
        arr[i + OFF][j + OFF] = 0


# ✅ 정답 출력: 남은 1들을 덮는 최소 직사각형(바운딩 박스) 넓이
found = False
min_x = min_y = 10**9
max_x = max_y = -10**9

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            found = True
            if i < min_x: min_x = i
            if i > max_x: max_x = i
            if j < min_y: min_y = j
            if j > max_y: max_y = j

if not found:
    print(0)
else:
    print((max_x - min_x + 1) * (max_y - min_y + 1))
