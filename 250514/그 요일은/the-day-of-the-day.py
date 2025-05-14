m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week=['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

month,day=m1,d1
current_day_index = 0

cnt_A=0

while True:

    # 현재 요일이 A와 같으면 카운트 증가
    if day_of_week[current_day_index] == A:
        cnt_A += 1

    if month == m2 and day==d2:
        break


    day += 1
    current_day_index= (current_day_index + 1) % 7

# 달 넘김 처리
    if day > num_of_days[month]:
        month += 1
        day = 1



print(cnt_A)