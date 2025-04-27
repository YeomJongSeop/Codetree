A=input()
B=input()

count=0
while A!=B:
    A=A[-1]+A[:-1]
    count+=1
    if count>=len(A):
        break

if count>0 and count<len(A):
    print(count)
else: print(-1)



