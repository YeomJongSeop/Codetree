n = int(input())
arr=[]

for _ in range(n):
    arr.append(tuple(input().split()))

li=[]

# Please write your code here.

for i in range(len(arr)):
    if arr[i][2]=='Rain':
        li.append(arr[i])


print(*min(li))