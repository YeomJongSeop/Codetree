MAX_K=1000
arr=[[0]*(2*MAX_K+1) for _ in range(2*MAX_K+1) ]

li_1=[ list(map(int,input().split()))]
li_2=[ list(map(int,input().split()))]

for a,b,c,d in li_1:
    for i in range(a,c):
        for j in range(b,d):
            arr[i][j]=1

for a,b,c,d in li_2:
    for i in range(a,c):
        for j in range(b,d):
            arr[i][j]=0

sero=abs(b-d)


for a,b,c,d in li_1:
    for i in range(a,c):
        cnt=0
        for j in range(b,d): # 열 계산
            if arr[i][j] ==1:
                cnt+=1

        if cnt !=sero and cnt>=1: # 열 카운팅으로 계산해서 직사각형 만들기
            for j in range(b,d):
                arr[i][j]=1
sum=0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        sum+=arr[i][j]


print(sum)