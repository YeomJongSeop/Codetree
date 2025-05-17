n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr=[0 for _ in range(201)]


for elem in segments:
    a,b = elem[0]+100,elem[1]+100
    for i in range(a,b+1):
        arr[i]+=1


print(max(arr))