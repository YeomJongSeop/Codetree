n = int(input())
blocks = [int(input()) for _ in range(n)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

# Please write your code here.


for _ in range(s1,e1+1):
    blocks.pop(s1-1)

for _ in range(s2,e2+1):
    blocks.pop(s2-1)


print(len(blocks))

for i in range(len(blocks)):
    print(blocks[i])