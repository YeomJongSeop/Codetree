import sys
input=sys.stdin.readline

s=list(input().rstrip())

for _ in range(2):
    for elem in s:
        print(elem,end='')
    print()

