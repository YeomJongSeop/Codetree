a, b = map(int, input().split())
n = list(input())

# Please write your code here.
arr=n[::-1]
t_num=0

for i in range(len(n)-1,-1,-1):
    t_num+= int(arr[i])*(a**i)


n=t_num

ans=[]

while True:
    if n<b:
        ans.append(n)
        break

    ans.append(n%b)
    n= n//b


for elem in ans[::-1]:
    print(elem,end='')


    