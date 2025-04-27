N= int(input())
arr=[input() for _ in range(N)]

length=0
count=[]

for elem in arr:
    length+=len(elem)
    if 'a' in elem[0]:
        count.append(elem)

print(length, len(count))