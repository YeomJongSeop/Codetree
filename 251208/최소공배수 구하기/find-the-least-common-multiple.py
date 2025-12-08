
#1
'''
import math

a,b= map(int,input().split())
lcm_value = math.lcm(a,b)

print(lcm_value)

'''

#2

a,b= map(int,input().split())

def make_gcd(a,b):
    while b:
	    a,b=b,a%b
    return a

def make_lcm(a,b):
    gcd_val =make_gcd(a,b) 
    return (a*b//gcd_val)

print(make_lcm(a,b))