a, b = map(int, input().split())

# Please write your code here.

def ans(a,b):
    s=['3','6','9']
    count=0

    for i in range(a,b+1):
        if i%3==0:
            count+=1
        else:
            arr=list(str(i))
            for elem in arr:
                if elem in s:
                    count+=1
    

    return(count)
        

print(ans(a,b))