Y, M, D = map(int, input().split())

# Please write your code here.
d_31=[1,3,5,7,8,10,12]
d_30=[4,6,9,11]


def is_yoon(Y):
    if Y%4==0:
        if Y%100==0:
            if Y%400==0:
                return True
            return False
        return True

    return False
        
   
def month_check(Y,M,D):
    
    if M in d_31:
        if D>31:
            return False
        return True

    elif M in d_30:
        if D>30:
            return False
        return True

    elif M == 2:
        if is_yoon(Y):
            if D>29:
                return False
            return True
        else:
            if D>28:
                return False
            return True

    else: return False

def final(Y,M,D):

    if month_check(Y,M,D):
        if M>=3 and M<=5:
            return 'Spring'
        elif M>=6 and M<=8:
            return 'Summer'
        elif M>=9 and M<=11:
            return 'Fall'
        else: return 'Winter'

    return -1


print(final(Y,M,D))
        

