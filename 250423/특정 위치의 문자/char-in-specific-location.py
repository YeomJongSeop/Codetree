N=input()

arr=['L', 'E', 'B', 'R', 'O', 'S']

for i in range(len(arr)):
    if arr[i]== N:
        print(i)
        break
    else: 
        if i ==len(arr)-1:
            print('None')
        continue

    

    