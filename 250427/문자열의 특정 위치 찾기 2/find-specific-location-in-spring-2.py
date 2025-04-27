N=input()

s=['apple','banana','grape','blueberry','orange']

ans=[]

for elem in s:
    if elem[2] ==N or elem[3]==N:
        ans.append(elem)
        print(elem)


print(len(ans))
