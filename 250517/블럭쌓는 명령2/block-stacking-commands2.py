n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.

block=[0 for _ in range(n)]


for elem in commands:
    a,b=elem[0]-1,elem[1]-1
    for i in range(a,b+1):
        block[i]+=1


print(max(block))