MAX_K = 1000
OFF = MAX_K
N = 2 * MAX_K + 1

arr = [[0] * N for _ in range(N)]

a1, b1, c1, d1 = map(int, input().split())
a2, b2, c2, d2 = map(int, input().split())

# 1번: 칠하기
for i in range(a1, c1):
    for j in range(b1, d1):
        arr[i + OFF][j + OFF] = 1

# 2번: 덮기(지우기)
for i in range(a2, c2):
    for j in range(b2, d2):
        arr[i + OFF][j + OFF] = 0

# 생각할때 좌표마다 1을 넣어주는것 (0,0) (6,0)이라면 
# 길이는 6이지만 좌표 이중 배열 넣어줄떄 [i][j]를 0~5 씩 넣어진다
# 이거때문에 인덱스를 기준으로 +1을 맨 마지막에 해줌 칸을 채우는것이랑 좌표길이랑 생각 잘하기

found=False
min_x =min_y = 10**9
max_x= max_y= -10**9

for i in range(N):
    for j in range(N):
        if arr[i][j] ==1:
            found=True
            if i<min_x: min_x=i
            if i>max_x: max_x=i
            if i<min_y: min_y=j
            if i>max_y: max_y=j


if not found:
    print(0)
else: # 중요 좌표로 변환해서 구하는 것이니까
    print((max_x - min_x + 1) * (max_y - min_y + 1 ))