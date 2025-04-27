a,b=map(int,input().split())

total=a+b

arr=list(str(total))

count=0
for elem in arr:
    if elem =='1':
        count+=1


print(count)    