import sys
input = sys.stdin.readline

N,M = map(int,input().split())

matrix1=[]
matrix2=[]
ans=[]
for _ in range(N):
    arr=[0]*M
    ans.append(arr)

for _ in range(N):
    arr=list(map(int,input().split()))
    matrix1.append(arr)


for _ in range(N):
    arr=list(map(int,input().split()))
    matrix2.append(arr)


for i in range(N):
    for m in range(M):
        if matrix1[i][m] != matrix2[i][m]:
            ans[i][m]=1

        

for i in range(N):
    for m in range(M):
        print(ans[i][m],end=' ')
    print()