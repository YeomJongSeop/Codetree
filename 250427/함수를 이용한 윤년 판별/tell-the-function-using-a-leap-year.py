y = int(input())

# Please write your code here.

def yoon_year(y):

    if y%4 ==0:
        if y%100==0 and y%400!=0:
            print('false')
        else: print('true')

    else: print('false')


yoon_year(y)
