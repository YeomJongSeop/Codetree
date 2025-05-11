import sys

INT_MIN = -1 * sys.maxsize
MAX_VALUE = 10000

n = int(input())

# dp[j] : 지금까지 마지막으로 고른 원소의 값이 j일 때의
# 최장 부분 수열의 길이
# 최대를 구하는 문제이므로, 초기에는 전부 INT_MIN을 넣어줍니다.
dp = [INT_MIN for _ in range(MAX_VALUE + 1)]

a = [0] + list(map(int, input().split()))

# 0번째 원소에 0이라는 숫자로 항상 부분 수열을 만들되
# 이때까지의 부분 수열의 길이는 0이었기 때문에, 
# 각각의 위치에 있는 원소를 시작으로 하는 
# 모든 부분 수열을 만들 수 있게 해줍니다.
dp[0] = 0

for i in range(1, n + 1):
    # j가 a[i]인 경우만 고민해서 누적합니다.
    j = a[i]
    for l in range(a[i]):
        if dp[l] != INT_MIN:
            dp[j] = max(dp[j], dp[l] + 1)

# 마지막으로 끝나는 숫자가 j일때의 부분 수열들 중
# 가장 길이가 긴 부분 수열을 고릅니다.
answer = 0
for j in range(MAX_VALUE + 1):
    answer = max(answer, dp[j])
    
print(answer)
