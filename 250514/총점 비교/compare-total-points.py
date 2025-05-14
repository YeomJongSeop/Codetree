n = int(input())

stu=[]

for _ in range(n):
    student_input = input().split()

    name= student_input[0]
    s1= int(student_input[1])
    s2= int(student_input[2])
    s3= int(student_input[3])

    stu.append((name,s1,s2,s3))



# Please write your code here.
stu.sort(key= lambda x:x[1]+x[2]+x[3])

for elem in stu:
    print(*elem)