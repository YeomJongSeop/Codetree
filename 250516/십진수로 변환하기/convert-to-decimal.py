binary = input()
ans=0
# Please write your code here.
arr = binary[::-1]


for i in range(len(binary)-1,-1,-1):
    ans+= int(arr[i])* (2**i)


print(ans)