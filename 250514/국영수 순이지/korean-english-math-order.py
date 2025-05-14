n = int(input())
stu=[]
for _ in range(n):
    info = input().split()
    name = info[0]
    kor=int(info[1])
    eng = int(info[2])
    math=int(info[3])
    stu.append((name,kor,eng,math))

# Please write your code here.

stu.sort(key = lambda x : (-x[1],-x[2],-x[3]))

for elem in stu:
    print(*elem)