month=[i for i in range(0,13)]
day=[0, 31,28,31,30,31,30,31,31,30,31,30,31]
day_of_week = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
day_sum=0

m1,d1,m2,d2 = map(int,input().split())


if m1 >m2:
    for i in range(m2,m1):
        day_sum +=day[i]
    day_sum=day_sum+d1-d2
    print(day_of_week[-day_sum%7])
elif m1==m2:
    if d1<=d2:
        print(day_of_week[abs(d1-d2)%7])
    else:
        print(day_of_week[-abs(d1-d2)%7])
else:
    for i in range(m1,m2):
        day_sum +=day[i]
    day_sum=day_sum-d1+d2
    print(day_of_week[day_sum%7])
    
