a, b = map(int, input().split())

# Please write your code here.
def modify(a,b):
    if a>b:
        a=2*a
        b=b+10
        return a,b

    else:
        b=2*b
        a=a+10
        return a,b

a,b=modify(a,b)

print(a,b)

