a=list(map(int,input().split()))

i=2
while len(a)<=9:
    a.append(a[i-1]+2*a[i-2])
    i+=1

for j in range(len(a)):
    print(a[j],end=' ')