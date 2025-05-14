a, b, c, d = map(int, input().split())

# Please write your code here.
hour,mins=a,b
el_time=0

while True:
    if hour == c and mins ==d:
        break
    
    el_time+=1
    mins+=1

    if mins==60:
        hour +=1
        mins=0


print(el_time)