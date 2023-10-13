s = input()
arr = []
char = ''
i = 0
j = 0
k = 0
for ch in s:
    if ch == 'L':
        i =i + 1
    elif ch == 'R':
        j = j + 1
    if i == j:
        arr.append(s[k:i+j])
        k=i+j
        
print(len(arr))
for c in arr:
    print(c)