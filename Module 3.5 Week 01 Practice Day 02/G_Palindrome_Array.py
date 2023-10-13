n = int(input())
a = list(map(int, input().split()))
i = 0
j = n-1
flag = 1
while i < n/2:
    l = a[i]
    r = a[j]
    if l != r:
        flag = 0
    i = i + 1
    j = j-1
if flag == 1:
    print("YES")
else: print("NO")