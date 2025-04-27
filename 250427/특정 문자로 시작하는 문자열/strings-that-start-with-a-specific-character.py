N=int(input())
arr=[input() for _ in range(N)]
alp=input()

count =0
length=0

for elem in arr:
    if alp in elem[0]:
        length+=len(elem)
        count+=1

avg=round(length/count,2)

print(count, f"{avg:.2f}" )





