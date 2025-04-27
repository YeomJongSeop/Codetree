A=input()
B=input()
ans=[]

for elem in B:
    if elem =='L':
        A = A[1:]+ A[0]

    elif elem =='R':
        A = A[-1]+A[:-1]

print(''.join(A))