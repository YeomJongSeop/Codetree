import sys
input=sys.stdin.readline

N=int(input())

arr_2d=[]

for _ in range(N):
    arr= [0]*N
    arr_2d.append(arr)


for i in range(N):
    arr_2d[0][i]=1
    arr_2d[i][0]=1


for i in range(1,N):
    for j in range(1,N):
        arr_2d[i][j]=arr_2d[i-1][j-1]+arr_2d[i][j-1]+arr_2d[i-1][j]

for row in arr_2d:
    for elem in row:
        print(elem,end=' ')
    print()