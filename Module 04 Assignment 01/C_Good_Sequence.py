n = int(input())
a = [int(x) for x in input().split()]
dic = {}
for i in a:
    if i not in dic:
        dic[i] = 1
    else: dic[i] = dic[i] + 1

result = 0
for key, value in dic.items():
    # print(key, value)
    if key < value:
        result = result + (value - key)
    elif key > value:
        # result = result + (key - value)
        result = result + value       
print(result)