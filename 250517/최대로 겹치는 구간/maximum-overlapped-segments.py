n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr=[0 for _ in range(201)] # -100~ 100


for elem in segments:
    a,b = elem[0]+100,elem[1]+100
    for i in range(a,b):
        arr[i]+=1


print(max(arr))