n = int(input())
a = [int(x) for x in input().split()]
def solve(a):
    for i in a:
        if i % 2 != 0:
            return 0
    return solve([i//2 for i in a])+1
print(solve(a))