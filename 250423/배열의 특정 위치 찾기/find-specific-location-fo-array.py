a=list(map(int,input().split()))

s=a[1::2]
s2=a[2::3]

print(sum(s), sum(s2)/len(s2))