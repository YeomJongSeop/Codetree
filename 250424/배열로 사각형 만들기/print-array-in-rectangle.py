import sys
input=sys.stdin.readline

arr_2d=[]

for _ in range(5):
    arr=[0]*5
    arr_2d.append(arr)


arr_2d[0][0]=1

for i in range(1,5):

    arr_2d[i][0]=1
    for j in range(1,5):
        arr_2d[0][j]=1
        arr_2d[i][j]=arr_2d[i-1][j]+arr_2d[i][j-1]


for row in arr_2d:
    for elem in row:
        print(elem,end=' ')
    print()




        
        