import sys
input = sys.stdin.readline

arr=[] # 질의 모음 리스트

N,Q = map(int,input().split())
l=list(map(int,input().split())) # 원소 모은 리스트



for i in range(Q):
    row=list(map(int,input().split()))
    arr.append(row)


for j in range(Q):
    if arr[j][0]==1:
        a=arr[j][1]
        print(l[a-1])

    elif arr[j][0]==2:
        b=arr[j][1]
        if b in l:
            print((l.index(b))+1)
            continue
        else: print(0)
        

     
    elif arr[j][0]==3:
        s= arr[j][1]-1
        e= arr[j][2]
        for c in range(s,e):
            print(l[c],end=' ')
        print()


    