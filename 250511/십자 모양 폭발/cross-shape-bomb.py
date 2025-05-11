n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

# 인덱스 조정 (1-indexed를 0-indexed로 변환)
r -= 1
c -= 1

# 십자 모양 방향 벡터 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def in_range(x, y):
    """격자 내부인지 확인"""
    return 0 <= x < n and 0 <= y < n

# 폭발 크기 가져오기
bomb_size = grid[r][c]

# 폭발할 위치 처리
grid[r][c] = 0  # 중심점 폭발
for direction in range(4):  # 4방향으로 폭발
    for size in range(1, bomb_size):
        nx = r + dx[direction] * size
        ny = c + dy[direction] * size
        if in_range(nx, ny):
            grid[nx][ny] = 0

# 중력 적용
for col in range(n):
    # 열 별로 남아있는 숫자들을 모으기
    numbers = []
    for row in range(n):
        if grid[row][col] != 0:
            numbers.append(grid[row][col])
    
    # 열 초기화
    for row in range(n):
        grid[row][col] = 0
    
    # 아래부터 채우기
    for i, num in enumerate(numbers):
        grid[n - len(numbers) + i][col] = num

# 결과 출력
for row in grid:
    print(*row)
