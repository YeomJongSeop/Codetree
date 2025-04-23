a=list(map(int,input().split()))

a_sum=0
if a[0]<250:
    for i in range(len(a)):
        a_sum+=a[i]
        if a[i]>250:
            a_sum -=a[i]
            print(a_sum,end=' ')
            print(round(a_sum/i,1))
            break
        elif a[len(a)-1]<250:
            print(a_sum, round(a_sum/len(a),1))
