a=list(input())

for i in range(len(a)):
    if a[i] =='e':
        a.pop(i)
        break


print(''.join(a))