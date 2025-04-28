n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def total(queries):
    s=[]
    for elem in queries:
        total=0
        a,b=elem
        for i in range(a-1,b):
            total+=arr[i]
        s.append(total)

    return s

    
for elem in total(queries):
    print(elem)


