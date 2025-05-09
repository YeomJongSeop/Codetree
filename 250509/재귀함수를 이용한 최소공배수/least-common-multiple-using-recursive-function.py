n = int(input())
arr = list(map(int, input().split()))

def gcd(a,b):
    if b == 0:
        return a
    
    return gcd(b,a%b)


def lcm(a,b):
    return a*b // gcd(a,b)

def lcm_recur(idx):
    if idx == n-1:
        return arr[idx]

    return lcm(arr[idx],lcm_recur(idx+1))

print(lcm_recur(0))