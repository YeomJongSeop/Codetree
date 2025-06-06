n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
dp=[[0]*n for _ in range(n)]



def initialize():
    dp[0][0]=grid[0][0]
    
    # 첫 열 초기화
    for i in range(1,n):
        dp[i][0]= dp[i-1][0]+grid[i][0]

    # 첫 행 초기화
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]

        
initialize()

# 나머지 DP 채우기
for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

print(dp[n-1][n-1])