n= int(input())
arr=list(map(int,input().split()))

ans=[]
for i in range( 0, len(arr),2):
    ans.append(arr[:i+1])


for j in range(len(ans)):
    mid= len(ans[j]) // 2
    ans[j].sort()
    print(ans[j][mid],end=' ')



    
