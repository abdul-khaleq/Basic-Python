n, q = map(int, input().split())
a = list(map(int, input().split()))
pre = []
pre.append(a[0])
for i in range(1, n):
    pre.append(a[i] + pre[i-1])
for _ in range(q):
    l, r = map(int, input().split())
    left = l-1
    right = r-1
    if left == 0:
        print(pre[right])
    elif left > 0:
        print(pre[right] - pre[left-1])
