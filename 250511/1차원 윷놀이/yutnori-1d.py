n, m, k = map(int, input().split())
nums = list(map(int, input().split()))
positions = [1] * k
max_count = 0

def backtrack(turn):
    global max_count
    if turn == n:
        current = sum(1 for pos in positions if pos >= m)
        max_count = max(max_count, current)
        return
    for i in range(k):
        if positions[i] >= m:
            continue
        positions[i] += nums[turn]
        backtrack(turn + 1)
        positions[i] -= nums[turn]

backtrack(0)
print(max_count)
