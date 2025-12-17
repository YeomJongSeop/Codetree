MAX_K=1000
arr=[[0]*(2*MAX_K+1) for _ in range(2*MAX_K+1) ]
OFF=MAX_K

a1,b1,c1,d1 = map(int, input().split())
a2,b2,c2,d2 = map(int, input().split())

# 1번: 칠하기
for i in range(a1, c1):
    for j in range(b1, d1):
        arr[i+OFF][j+OFF] = 1

# 2번: 지우기
for i in range(a2, c2):
    for j in range(b2, d2):
        arr[i+OFF][j+OFF] = 0

sero=abs(b1-d1)



for i in range(a1,c1):
    cnt=0
    for j in range(b1,d1): # 열 계산
        if arr[i+OFF][j+OFF] ==1:
            cnt+=1

    if cnt !=sero and cnt>=1: # 열 카운팅으로 계산해서 직사각형 만들기
        for j in range(b1,d1):
            arr[i+OFF][j+OFF]=1

sum=0

for i in range(len(arr)):
    for j in range(len(arr[0])):
        sum+=arr[i][j]


print(sum)