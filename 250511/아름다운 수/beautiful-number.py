n = int(input())
count = 0

def backtrack(pos):
    global count
    if pos == n:
        count += 1
        return
    if pos > n:
        return
    for d in range(1, 5):
        if pos + d <= n:
            backtrack(pos + d)

backtrack(0)
print(count)
