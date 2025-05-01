N = int(input())

# Please write your code here.

def cnt1(n):


    if n==1:
        return 0
    
    elif n%2==0:

        return cnt1(n/2)+1
    else:

        return cnt1(n//3)+1




print(cnt1(N))