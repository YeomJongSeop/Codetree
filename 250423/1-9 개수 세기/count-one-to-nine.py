N=int(input())
a=list(map(int,input().split()))

count=[0]*10

for i in a:
    count[i]+=1


for j in range(1,len(count)):
    print(count[j])


