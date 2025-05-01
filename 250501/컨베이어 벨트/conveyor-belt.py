n, t = map(int, input().split())
u = list(map(int, input().split()))
d = list(map(int, input().split()))

# Please write your code here.
# 배열 미는 연산 할떄 마지막 원소 부터 밀어줘야!! 백업가는해짐

for _ in range(t):

    temp1 = u[n-1]
    temp2= d[n-1]
    for i in range(n-1,0,-1):
        u[i]=u[i-1]
    u[0]= temp2
    for j in range(n-1,0,-1):
        d[j]=d[j-1]
    d[0]= temp1


for i in range(n):
    print(u[i], end=' ')

print()
    
for i in range(n):
    print(d[i], end=' ')










    
    





