n = int(input())
a = list(map(int, input().split()))

min_idx = a.index(min(a))
max_idx = a.index(max(a))
a[min_idx], a[max_idx] = a[max_idx], a[min_idx]

for i in range(0, n):
    print(a[i], end=' ')
