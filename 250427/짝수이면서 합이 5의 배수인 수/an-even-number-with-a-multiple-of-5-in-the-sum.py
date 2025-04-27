n = int(input())

# Please write your code here.
def even_mul5(n):
    n_str=list(str(n))
    arr=[int(i) for i in n_str]

    if (n%2)==0 and (sum(arr)%5) ==0:
        print('Yes')


    else: print('No') 


even_mul5(n)