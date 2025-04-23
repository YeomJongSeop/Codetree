N=int(input())
a=list(map(float,input().split()))

avg=(round(sum(a)/N,1))
print(avg)

if avg >=4.0:
    print('Perfect')

elif avg>=3.0:
    print('Good')

else: print('Poor')