t = int(input())
for i in range(t):
    n = input()
    arr = []
    for c in n:
        arr.append(c)
    arr.reverse()
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print( "")