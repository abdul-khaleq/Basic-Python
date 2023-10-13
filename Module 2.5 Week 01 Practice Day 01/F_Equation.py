def calculate_S(X, N):
    S = 0
    power = 0
    
    for i in range(0, N+1, 2):
        S += X**i
        power = i
    
    if power == 0:
        S -= 1
        
    return S

# Read input
X, N = map(int, input().split())

# Calculate and print the result
result = calculate_S(X, N)
print(result)
