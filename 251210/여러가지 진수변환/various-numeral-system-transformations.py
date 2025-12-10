N,B=map(int,input().split())

ans=[]

while N>0:
    ans.append(N%B) 
    N=N//B   


#print(ans)

for i in range(len(ans)-1,-1,-1):
    print(ans[i],end='')