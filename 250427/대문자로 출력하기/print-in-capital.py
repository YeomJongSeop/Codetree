arr=list(input())
ans=[]


for i in range(len(arr)):
    if arr[i].isalpha():
        ans.append(arr[i].upper())


print(''.join(ans))