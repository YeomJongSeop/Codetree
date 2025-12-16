N = int(input())
li = [list(input().split()) for _ in range(N)]

MAX_K = 10000
# 변수 선언 및 입력:

# 0: no 1: white 2:black 3: gray
state = [0] * (2*MAX_K+1)

b_cnt = [0] * (2*MAX_K+1)
w_cnt = [0] * (2*MAX_K+1)

cur = MAX_K

for x, y in li:
    x=int(x)
    if y == 'R':  # 검정
        nxt = cur + x-1
        for i in range(cur, nxt+1):
            b_cnt[i] += 1
            state[i] = 2
        cur = nxt

    elif y == 'L':
        nxt = cur - x+1
        for i in range(nxt, cur+1):
            w_cnt[i] += 1
            state[i] = 1
        cur = nxt

w = 0
b = 0
g = 0

for i in range(len(state)):
    if w_cnt[i] >= 2 and b_cnt[i] >= 2:
        state[i] = 3
    if state[i] == 1:
        w += 1
    elif state[i] == 2:
        b += 1
    elif state[i] == 3:
        g += 1

print(w, b, g)
