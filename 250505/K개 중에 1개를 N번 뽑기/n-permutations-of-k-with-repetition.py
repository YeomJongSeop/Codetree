K, N = map(int, input().split())

# Please write your code here.
answer = []

def choose(curr_num):
    if curr_num == N:
        print(' '.join(map(str, answer)))
        return
    for i in range(1, K + 1):
        answer.append(i)
        choose(curr_num + 1)
        answer.pop()

choose(0)