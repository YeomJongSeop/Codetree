N, M = map(int, input().split())

def backtrack(start, current):
    if len(current) == M:
        print(' '.join(map(str, current)))
        return
    for i in range(start, N + 1):
        backtrack(i + 1, current + [i])

backtrack(1, [])
