n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Please write your code here.

students.sort(key=lambda x: (x[0],x[1]),reverse= True)


for student in students:
    print(*student)