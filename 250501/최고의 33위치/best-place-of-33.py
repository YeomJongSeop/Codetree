n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.

s=[]

def in_range(x,y):
    return 0<=x and x<n and 0<=y and y<n


# 3x3 영역 동전 반환
def coin_num(row,col): # row+2, col+2
    gold_count=0
    for i in range(row,row+3):
        for j in range(col,col+3):
            if in_range(i,j) and grid[i][j]==1: # 격자위치가 1이면 
                gold_count+=1
                
    
    return gold_count

# 탐색
for i in range(n-2):
    for j in range(n-2):
        s.append(coin_num(i,j))
    
print(max(s))


