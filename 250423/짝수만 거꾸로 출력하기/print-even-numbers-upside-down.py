N= int(input())
a=list(map(int,input().split()))

s=[]
for i in a:
    if i%2==0:
        s.append(i)

s=s[::-1]

for j in range(len(s)):
    print(s[j],end=' ')