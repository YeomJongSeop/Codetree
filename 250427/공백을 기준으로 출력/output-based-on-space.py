s=[input().split() for _ in range(2)]

answer=''
for i in range(len(s)):
    for j in range(len(s[i])):
        answer+=s[i][j]

print(answer)