n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

block=[0 for _ in range(n)]


for elem in commands:
    a,b=elem[0],elem[1]
    block[a-1]+=1
    block[b-1]+=1


print(max(block))