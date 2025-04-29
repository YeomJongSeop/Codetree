n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]


# 방향에 따른 이동량 설정
x, y = 0, 0

dx = {'E': 1, 'W': -1, 'N': 0, 'S': 0}
dy = {'E': 0, 'W': 0, 'N': 1, 'S': -1}

for move in moves:
    direction = move[0]
    distance = int(move[1])
    x += dx[direction] * distance
    y += dy[direction] * distance

print(x, y)