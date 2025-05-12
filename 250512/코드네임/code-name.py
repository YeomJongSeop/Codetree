import sys
arr=[]

for _ in range(5):
    n,s=input().split()
    arr.append((n,int(s)))

min_v= sys.maxsize

for i in range(5):
    if arr[i][1] < min_v:
        min_v =arr[i][1]
        idx=i

print(*arr[idx])


'''
import sys

class person:
    def __init__(self, name, score):
        self.name=name
        self.score=score


arr=[]

for _ in range(5):
    n,s=input().split()
    arr.append(person(n,int(s)))

min_v= sys.maxsize

for i in range(5):
    if arr[i].score < min_v:
        min_v =arr[i].score
        idx=i

print(arr[idx].name,arr[idx].score)
'''