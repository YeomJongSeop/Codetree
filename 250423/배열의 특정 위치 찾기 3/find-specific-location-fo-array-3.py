a=list(map(int,input().split()))


for i in range(len(a)):
    if a[i]==0:
        total=a[i-1]+a[i-2]+a[i-3]
        print(total)
        break
        
