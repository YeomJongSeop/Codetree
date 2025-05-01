n = int(input())

# Please write your code here.

def recur_dec(x):
    if x==0:
        return

    print(x,end=' ')
    recur_dec(x-1)

def recur_inc(x):
    if x==0:
        return

    recur_inc(x-1)
    print(x,end=' ')




recur_inc(n)
print()
recur_dec(n)