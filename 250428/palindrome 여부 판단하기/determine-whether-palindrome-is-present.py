A = input()

# Please write your code here.

def is_pal(A):
    arr=list(A)
    arr2=[]

    for i in range(len(arr)-1,-1,-1):
        arr2.append(arr[i])



    if arr == arr2:

        return True
    
    return False

if is_pal(A):
    print('Yes')
else: print('No')