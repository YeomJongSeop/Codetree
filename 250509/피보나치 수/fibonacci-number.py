N = int(input())

# Please write your code here.

max_num=45
dp= [0 for _ in range(max_num+1)]

dp[1]=dp[2]=1

memo=[-1 for _ in range(max_num+1)]

# 메모이제이션
def fibbo(n):
    if memo[n] != -1:        # 이미 n번째 값을 구해본 적이 있다면
        return memo[n]       # memo에 적혀있는 값을 반환해줍니다.
    if n <= 2:               # n이 2이하인 경우에는 종료 조건이므로 
        memo[n] = 1          # 해당하는 숫자를 memo에 넣어줍니다.
    else:                    # 종료조건이 아닌 경우에는 
        memo[n] = fibbo(n - 1) + fibbo(n - 2)  # 점화식을 이용하여 답을 구한 뒤
                                               # 해당 값을 memo에 저장해줍니다.
    return memo[n]                             # memo 값을 반환합니다.

#tabulation
for i in range(3,N+1):
    dp[i]=dp[i-1]+dp[i-2]

print(dp[N])
# print(fibbo(N))
