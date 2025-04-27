a=list(input())
b=list(input())

arr1=[]
arr2=[]

for i in range(len(a)):
    if a[i].isdigit():
        arr1.append(a[i])

for i in range(len(b)):
    if b[i].isdigit():
        arr2.append(b[i])


a_sum=int(''.join(arr1))
b_sum=int(''.join(arr2))

print(a_sum+b_sum)