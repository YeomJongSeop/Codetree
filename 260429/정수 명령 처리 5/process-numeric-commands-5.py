n = int(input())
arr = []

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push_back":
        arr.append(int(cmd[1]))

    elif cmd[0] == "pop_back":
        arr.pop()

    elif cmd[0] == "size":
        print(len(arr))

    elif cmd[0] == "get":
        k = int(cmd[1])
        print(arr[k - 1])