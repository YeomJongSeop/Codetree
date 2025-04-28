text = input()
pattern = input()

# Please write your code here.
def find_idx(text,pattern):
    a=len(pattern)
    for i in range(len(text)):
        if text[i:i+a]==pattern:
            return i
    return -1
    

    
print(find_idx(text,pattern))
