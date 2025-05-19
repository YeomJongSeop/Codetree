N,M = map(int,input().split())

A_move=[ tuple(input().split()) for _ in range(N) ]
B_move=[ tuple(input().split()) for _ in range(M) ]

A_pos=[0 for _ in range(100000)]
B_pos=[0 for _ in range(100000)]

idx=50000
time=0

for d,move in A_move:
    if d == 'R':
        for t in range(1,int(move)+1):
            idx+=1
            A_pos[time+t] = idx


    else:
        for t in range(1,int(move)+1):
            idx-=1
            A_pos[time+t] = idx
    time+= int(move)


idx=50000
time=0

for d,move in B_move:
    if d == 'R':
        for t in range(1,int(move)+1):
            idx+=1
            B_pos[time+t] = idx


    else:
        for t in range(1,int(move)+1):
            idx-=1
            B_pos[time+t] = idx
    time+= int(move)


for t in range(1,time+1):
    if A_pos[t] == B_pos[t]:
        print(t)
        break

else: print(-1)