
class program:
    def __init__(self,code,color,second):
        self.code = code
        self.color = color
        self.second = second

a,b,c = input().split()
pro1 = program(a,b,c)
print(f"code : {pro1.code} ")
print(f"color : {pro1.color} ")
print(f"second : {pro1.second} ")


