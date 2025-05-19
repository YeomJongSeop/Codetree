N,T = map(int,input().split())

arr= list(map(int, input().split()))

cnt=0
ans=[]

for elem in arr:
    if elem>T:
        cnt+=1
    else:
        ans.append(cnt)
        cnt=0

ans.append(cnt)

print(max(ans))


