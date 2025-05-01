N = int(input())

# Please write your code here.

def piv(n):
    if n==1:
        return 1
    if n==2:
        return 1

    return piv(n-1)+piv(n-2)

print(piv(N))