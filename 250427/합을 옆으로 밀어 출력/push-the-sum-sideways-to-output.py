N=int(input())

s=[int(input()) for _ in range(N)]

ans=str(sum(s))


print(ans[1:]+ans[0])