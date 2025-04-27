a=input()

arr=[]
for i in range(1,len(a),2):
    arr.append(a[i])

arr=arr[::-1]

for elem in arr:
    print(elem,end='')