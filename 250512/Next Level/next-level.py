user2_id, user2_level = input().split()
user2_level = int(user2_level)

# Please write your code here.
class User:
    def __init__(self, u_id='codetree',u_level=10):
        self.u_id = u_id
        self.u_level =u_level


user1=User()
user2=User(user2_id, user2_level)

print(f"user {user1.u_id} lv {user1.u_level}")
print(f"user {user2.u_id} lv {user2.u_level}")
