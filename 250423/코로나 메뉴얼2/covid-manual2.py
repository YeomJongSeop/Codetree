s=[]

for _ in range(3):
    row=list(input().split())
    s.append(row)

# A,B,C,D 진료소 카운트
count=[0]*4

for i in range(3):
    if s[i][0] == 'Y':
        tem=int(s[i][1])
        if tem>=37:
            count[0]+=1
        else:
            count[2]+=1
    elif s[i][0] == 'N':
        tem=int(s[i][1])
        if tem>=37:
            count[1]+=1
        else:
            count[3]+=1

if count[0]>=2:
    for j in range(len(count)):
        print(count[j],end=' ')
    print('E')

else:
    for j in range(len(count)):
        print(count[j],end=' ')


