n = int(input())

# Please write your code here
visited = [False] * (n+1)
selected_nums = []

# Function to generate all permutations
def generate_permutation(cnt):
    # Base case: we've selected n numbers
    if cnt == n+1:
        # Print the current permutation
        for num in selected_nums:
            print(num, end=" ")
        print()
        return
    
    # Try placing each number from 1 to n at the current position
    for i in range(1, n+1):
        # Skip if this number is already used
        if visited[i]:
            continue
            
        # Choose this number
        visited[i] = True
        selected_nums.append(i)
        
        # Recursively generate permutations for the next position
        generate_permutation(cnt+1)
        
        # Backtrack: undo our choice to try other possibilities
        selected_nums.pop()
        visited[i] = False

# Start generating permutations from position 1
generate_permutation(1)
