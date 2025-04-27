n,A = input().split()

arr=[input() for _ in range(int(n))]

count=0
for elem in arr:
    if elem == A:
        count+=1

print(count)
