a=input().split()

idx=-1

for i in range(len(a[0])):
    if a[1] in a[0][i]:
        print(i)
        break