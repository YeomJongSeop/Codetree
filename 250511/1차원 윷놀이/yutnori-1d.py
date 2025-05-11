n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
positions = [1] * k
max_count = 0

# 남은 이동 횟수에 대한 누적 합 계산
suffix_sums = [0] * (n + 1)
for i in range(n-1, -1, -1):
    suffix_sums[i] = suffix_sums[i+1] + nums[i]

def backtrack(turn):
    global max_count
    if turn == n:
        current = sum(1 for pos in positions if pos >= m)
        max_count = max(max_count, current)
        return
    
    remaining_sum = suffix_sums[turn]
    
    for i in range(k):
        if positions[i] >= m:
            continue
        # 남은 이동으로 목표 달성 불가 시 가지치기
        if positions[i] + remaining_sum < m:
            continue
        positions[i] += nums[turn]
        backtrack(turn + 1)
        positions[i] -= nums[turn]

backtrack(0)
print(max_count)
