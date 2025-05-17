n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
direc = []


# Please write your code here.
black=[0 for _ in range(100)]
white=[0 for _ in range(100)]

for elem in commands:
    if elem[1] =='R':
        for i in range(int(elem[0])):
            black[i]=1
            white[i]=0
    else:
        for i in range(int(elem[0])):
            white[i]=1
            black[i]=0


print(sum(white),sum(black))