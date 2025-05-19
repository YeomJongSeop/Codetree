N= int(input())
arr=[int(input()) for _ in range(N)]

ans=[]
cnt=1
for i in range(len(arr)):
    if arr[i] == arr[i-1]:
        cnt+=1
    else: 
        ans.append(cnt)
        cnt=1

print(max(ans))
