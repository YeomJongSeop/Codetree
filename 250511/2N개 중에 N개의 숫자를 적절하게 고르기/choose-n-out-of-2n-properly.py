n = int(input())
num = list(map(int, input().split()))
total = sum(num)
ans = float('inf')

def backtrack(index, cnt, curr_sum):
    global ans
    remaining = len(num) - index
    if cnt > n or cnt + remaining < n:
        return
    if index == len(num):
        if cnt == n:
            ans = min(ans, abs(total - 2 * curr_sum))
        return
    backtrack(index + 1, cnt + 1, curr_sum + num[index])
    backtrack(index + 1, cnt, curr_sum)

backtrack(0, 0, 0)
print(ans)
