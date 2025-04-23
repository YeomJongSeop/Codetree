import sys
input = sys.stdin.readline
s=[]
total=[]
for _ in range(4):
    arr=list(map(int,input().split()))
    s.append(arr)

for i in range(4):
    for j in range(4):
        if i>=j:
            total.append(s[i][j])

print(sum(total))

