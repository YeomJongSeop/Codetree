import sys
input= sys.stdin.readline

N, M= map(int,input().split())

arr=[]
c=1

for _ in range(N):
    row=[0]*M
    arr.append(row)


for i in range(N):
    for j in range(M):
        arr[i][j]=c
        print(arr[i][j],end=' ')
        c+=1
    print()



        