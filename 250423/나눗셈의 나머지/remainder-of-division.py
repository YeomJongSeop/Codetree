A,B=map(int,input().split())

s=[]
count=[0]*B

r=[]
total =0 


while A >=1:
    r.append(A%B)
    A= A//B



for i in r:
    count[i]+=1


for j in range(len(count)):
    total+=count[j]**2

print(total)

