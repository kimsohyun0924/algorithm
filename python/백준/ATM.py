person = int(input())
minute = list(map(int, input().split()))
 
num = 0

minute.sort()

for i in range(1, person):
    minute[i] += minute[i-1]

print(sum(minute))