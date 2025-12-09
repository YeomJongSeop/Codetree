A,B,C = map(int,input().split())
day=11
hour=11
minute=11
ans=0

if A< 11:
    print(-1)
elif A ==11 and B<11:
    print(-1)

elif A==11 and B==11 and C<11:
    print(-1)
else:
    if A>=11 and B>=11 and C>=11:
        ans=(((A-11)*60*24) + ((B-11)*60)+(C-11))
print(ans)