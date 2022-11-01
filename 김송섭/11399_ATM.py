# 작은걸 앞으로해서 중복하여 더해주기

number_of_people = int(input())
times = sorted(list(map(int, input().split())))
min_total = 0
for i in range(1, number_of_people + 1):
    for j in range(i):
        min_total += times[j]

print(min_total)