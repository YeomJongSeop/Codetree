a=list(map(int,input().split()))

a_sum=0
count=0

for i in range(len(a)):
    if a[i]>=250:
        break
    a_sum+=a[i]
    count+=1


print(a_sum, round(a_sum/count,1))