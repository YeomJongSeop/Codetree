n = int(input())
commands = [tuple(input().split()) for _ in range(n)]


# Please write your code here.
white=[0 for _ in range(2000)] 
black=[0 for _ in range(2000)]

idx=1000


for elem in commands:
    num= int(elem[0])
    if elem[1] =='R':
        for i in range(idx,idx+num):
            black[i]=1
            white[i]=0
        idx=idx+num-1

            
    else: # 좌측
        for i in range(idx,idx-num,-1):
            white[i]=1
            black[i]=0
        idx=idx-num+1


print(sum(white),sum(black))