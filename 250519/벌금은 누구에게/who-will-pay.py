N,M,K = map(int, input().split())
arr= [int(input()) for _ in range(M)]

# 학생 번호 별 벌칙 횟수 
stu_cnt =[0 for _ in range(N+1)] 

for i in range(len(arr)):
    stu_cnt[arr[i]]+=1

    if stu_cnt[arr[i]] ==K:
        print(arr[i])
        break
    
else: print(-1)
