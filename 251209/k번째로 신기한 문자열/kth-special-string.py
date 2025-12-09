N,K,T=input().split()
w_li=[input() for _ in range(int(N))]

ans=[]


for i in range(len(w_li)):

        # 단어 길이가 T보다 짧으면 패스
    if len(w_li[i]) < len(T):
        continue
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