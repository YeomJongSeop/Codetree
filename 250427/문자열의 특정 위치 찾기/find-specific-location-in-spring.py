a=input().split()


for i in range(len(a[0])):
    if a[0][i]==a[1]:
        print(i)
        break
else: print('No')

#if a[1] in a[0]:
    #print(a[0].index(a[1]))
#else: print('No')