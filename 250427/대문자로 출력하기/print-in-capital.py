arr=list(input())
ans=[]


for i in range(len(arr)):
    if arr[i] >='A' and arr[i]<='z':
        ans.append(arr[i].upper())


print(''.join(ans))