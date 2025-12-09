A,B,C = map(int,input().split())

ans=0

if (A, B, C) < (11, 11, 11):
    print(-1)

else:
    ans=(((A-11)*60*24) + ((B-11)*60)+(C-11))
    print(ans)
        

