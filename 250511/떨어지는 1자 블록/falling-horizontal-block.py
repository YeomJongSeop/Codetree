n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# k를 0-indexed로 변환
k -= 1

# 블록이 떨어질 위치 찾기
row = 0
while row < n:
    # 바닥에 도달했는지 확인
    if row == n - 1:
        break
    
    # 다음 행에 블록이 있는지 확인
    has_block = False
    for col in range(k, k + m):
        if grid[row + 1][col] == 1:
            has_block = True
            break
    
    # 다음 행에 블록이 있으면 현재 위치에 멈춤
    if has_block:
        break
    
    # 다음 행으로 이동
    row += 1

# 블록 배치하기
for col in range(k, k + m):
    grid[row][col] = 1

# 결과 출력
for row in grid:
    print(*row)
