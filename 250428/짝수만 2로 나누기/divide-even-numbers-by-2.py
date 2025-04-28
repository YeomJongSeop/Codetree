n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def dev_2(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i] = int(arr[i]/2)

    return arr
    

ans= dev_2(arr[:])

for elem in ans:
    print(elem,end=' ')
