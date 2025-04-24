import sys
input=sys.stdin.readline

N=int(input())

m=[]

for _ in range(N):
    arr=[0]*N
    m.append(arr)

num=1
count=0 # 방향전환 시키는 변수

for i in range(N-1,-1,-1):
    if count%2 ==0: #count가 짝수일 떄
        count+=1
        for j in range(N-1,-1,-1):
            m[j][i]=num
            num+=1
    else: # count가 홀수
        count+=1
        for j in range(N):
            m[j][i]=num
            num+=1
            


for row in m:
    for elem in row:
        print(elem,end=' ')
    print()