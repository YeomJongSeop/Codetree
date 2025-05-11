UNUSED = -1

str1 = input()
str2 = input()

str1_len, str2_len = len(str1), len(str2)
str1, str2 = '#' + str1, '#' + str2

memo = [[UNUSED] * (str2_len + 1) for _ in range(str1_len + 1)]

def find_max_len(i, j):
    if i > str1_len or j > str2_len:
        return 0
    if memo[i][j] != UNUSED:
        return memo[i][j]
    if str1[i] == str2[j]:
        memo[i][j] = find_max_len(i + 1, j + 1) + 1
    else:
        memo[i][j] = max(find_max_len(i + 1, j), find_max_len(i, j + 1))
    return memo[i][j]

print(find_max_len(1, 1))