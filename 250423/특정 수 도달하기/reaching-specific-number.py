a=list(map(int,input().split()))

a_sum=0
if a[0]<250:
    for i in range(len(a)):
        a_sum+=a[i]
        if a_sum>=260:
            a_sum -=a[i]
            print(a_sum,end=' ')
            print(round(a_sum/i,1))
            break
