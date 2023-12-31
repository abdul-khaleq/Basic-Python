def count_xyz_combinations(K, S):
    count = 0

    for X in range(K+1):
        for Y in range(K+1):
            Z = S - X - Y
            if 0 <= Z <= K:
                count += 1

    return count

# Read input
K, S = map(int, input().split())


# Calculate and print the result
result = count_xyz_combinations(K, S)
print(result)
