secret_code, meeting_point, time = input().split()
time = int(time)

# Please write your code here.

class Scode:
    def __init__(self, secret_code, meeting_point, time):
        self.s = secret_code
        self.m = meeting_point
        self.t = time


scode1 = Scode(secret_code, meeting_point, time)

print(f"secret code : {scode1.s}")
print(f"meeting point : {scode1.m}")
print(f"time : {scode1.t}")
