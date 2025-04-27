s=[input() for _ in range(3)]

max1=0
min1=float('inf')
for i in s:
    if len(i)>max1:
        max1=len(i)
    if len(i)<min1:
        min1=len(i)


print(max1-min1)