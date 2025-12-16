offset=50
arr=[0]*101
N=int(input())
li=[list(input().split()) for _ in range(N) ]


cur = offset
for x,y in li:
    x=int(x)
    if y =='L':
        nxt=cur-x
        for i in range(nxt,cur):
            arr[i]+=1
        cur=nxt
    else:
        nxt=cur+x
        for i in range(cur,nxt):
            arr[i]+=1
        cur=nxt
             
             
cnt = 0
for v in arr:
    if v >= 2:
        cnt += 1
print(cnt)