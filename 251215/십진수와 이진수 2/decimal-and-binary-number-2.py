
N=input()

li=str(N)
li_r=li[::-1]

num=0
for i in range(len(li_r)):
    num+= (int(li_r[i])*(2**i))


a=0
a=num*17

#이진수 표현
ans=[]
while a>0:
    ans.append(a%2)
    a=a//2    

ans=ans[::-1]
for enum in ans:
    print(enum,end='')
