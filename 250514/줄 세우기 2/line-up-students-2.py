n= int(input())

li=[]

for i in range(n): 
    row=tuple(map(int,input().split())) + (i+1,)  # (i+1,) 1개의 원소를 가진 튜플(tuple)
    li.append(row)

li.sort(key= lambda x:(x[0],-x[1]))

for elem in li:
    print(*elem)
