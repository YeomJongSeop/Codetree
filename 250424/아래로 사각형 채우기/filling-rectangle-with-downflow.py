import sys
input=sys.stdin.readline


N=int(input())

m=[]

for _ in range(N):
    arr=[0]*N
    m.append(arr)


for i in range(N):
    m[i][0]=i+1
    for j in range(1,N):
        m[i][j]=m[i][j-1]+N 

for i in range(N):
    for j in range(N):
        print(m[i][j],end=' ')
    print()
        

