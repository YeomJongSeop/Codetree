import sys
input=sys.stdin.readline

N,M= map(int,input().split())

arr_2d=[[0 for _ in range(N)] for _ in range(N)
]

for _ in range(M):
    r,c=tuple(map(int,input().split()))
    arr_2d[r-1][c-1]=r*c

for row in arr_2d:
    for elem in row:
        print(elem,end=' ')
    print()

