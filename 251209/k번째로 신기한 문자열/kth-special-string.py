N,K,T=input().split()
w_li=[input() for _ in range(int(N))]

ans=[]


for i in range(len(w_li)):
    ok=True
    for j in range(len(T)):
        if w_li[i][j]!=T[j]:
            ok=False

    if ok ==True:
        ans.append(w_li[i]) 

        

ans=set(ans)
ans=list(ans)
ans.sort()
#print(ans)

print(ans[int(K)-1])