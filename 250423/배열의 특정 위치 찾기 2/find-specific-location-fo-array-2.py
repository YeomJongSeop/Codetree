a=list(map(int,input().split()))
total_odds= sum(a[0::2])
total_evens= sum(a[1::2])

print(abs(total_odds-total_evens))

