N = int(input())

# Please write your code here.

def ssum(n):
    if n < 10:
        return n*n
    
    return (n % 10) ** 2 + ssum(n // 10)

print(ssum(N))