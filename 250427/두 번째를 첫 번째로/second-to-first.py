a=list(input())

alp=a[1]

for i in range(1,len(a)):
    if a[i] == alp:
        a[i]=a[0]

print(''.join(a))

