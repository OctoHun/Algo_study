number_of_people = int(input())
levels = [1] * number_of_people
specs = []
for _ in range(number_of_people):
    specs.append(list(map(int, input().split())))

for i in range(number_of_people):
    for j in range(number_of_people):
        if specs[i][0] < specs[j][0]:
            if specs[i][1] < specs[j][1]:
                levels[i] += 1

print(*levels)