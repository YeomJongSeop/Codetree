n = int(input())

# Please write your code here.


def n_sum(n):
    total=0
    for i in range(n+1):
        total+=i

    return total//10


print(n_sum(n))
