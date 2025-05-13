n = int(input())

student=[]

for _ in range(n):
    tu = tuple(input().split())
    student.append(tu)


# Please write your code here.

student.sort(key=lambda x:x[1])

for i in range(len(student)):
    print(*student[i])