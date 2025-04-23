a= list(map(int, input().split()))

i=1
while len(a)<=9:
    a.append((a[i-1]+a[i])%10)
    i+=1


for j in range(len(a)):
    print(a[j],end=' ')

