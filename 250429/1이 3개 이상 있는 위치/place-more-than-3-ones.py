n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.


# 격자에서 열 탐색 방향(동남서북)-행렬 생각
dxs = [0, 1, 0, -1] #행번호
dys = [1, 0, -1, 0] #열번호

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n



def count3_over(grid):
    ans = 0
    for x in range(n):
        for y in range(n):
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and grid[nx][ny] == 1:
                    cnt += 1
            if cnt >= 3:
                ans += 1
    return ans

print(count3_over(grid))

        




