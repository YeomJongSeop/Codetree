N=int(input())
a=list(map(int,input().split()))
a.sort()
b=[]

c=[]
for i in range(len(a)//2):
    b.append([a[i],a[len(a)-1-i]])

for j in range(len(b)):
    c.append(sum(b[j]))

print(max(c))