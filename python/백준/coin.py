n, k = map(int, input().split())

value = list()

num = 0

for i in range(n):
    value.append(int(input()))

for i in reversed(range(n)):
    if k > value[i]:
        num += k//value[i] 
        k = k%value[i]


print(num)
