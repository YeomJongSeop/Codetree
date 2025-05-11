n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 8방향 정의 (시계방향 순서)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

def find_position(num):
    """숫자의 위치를 찾는 함수"""
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return i, j

def is_valid(x, y):
    """좌표가 격자 내에 있는지 확인하는 함수"""
    return 0 <= x < n and 0 <= y < n

# m번 반복
for _ in range(m):
    # 1부터 n*n까지의 숫자를 순서대로 처리
    for num in range(1, n*n + 1):
        # 현재 숫자의 위치 찾기
        x, y = find_position(num)
        
        # 인접한 8방향 중 가장 큰 값 찾기
        max_val = 0
        max_x, max_y = x, y
        
        for i in range(8):
            nx, ny = x + dx[i], y + dy[i]
            
            # 격자 범위 밖이면 무시
            if not is_valid(nx, ny):
                continue
            
            # 더 큰 값을 찾으면 갱신
            if grid[nx][ny] > max_val:
                max_val = grid[nx][ny]
                max_x, max_y = nx, ny
        
        # 가장 큰 인접 값과 교환
        grid[x][y], grid[max_x][max_y] = grid[max_x][max_y], grid[x][y]

# 결과 출력
for row in grid:
    print(*row)
