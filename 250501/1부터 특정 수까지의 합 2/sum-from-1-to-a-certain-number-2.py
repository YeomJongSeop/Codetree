N = int(input())

# Please write your code here.

def summ(n):
    if n == 1:
        return 1

    return summ(n - 1) + n


print(summ(N))