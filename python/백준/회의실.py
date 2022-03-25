n = int(input())
s = []

num = 0
last = 0

for i in range(n):
    first, second = map(int, input().split())
    s.append([first, second])

s = sorted(s, key=lambda a: a[0])
s = sorted(s, key=lambda a: a[1])

last = 0

for i in range(n):
    if s[i][0] > last:
        num += 1
        last = s[i][1]

print(num)