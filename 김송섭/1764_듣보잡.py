no_one_hear_people, no_one_saw_people = map(int, input().split())

no_one_hear_and_saw_people = {}

for _ in range(no_one_hear_people):
    people = input()
    no_one_hear_and_saw_people[people] = 0

count = 0
no_one = []
for _ in range(no_one_saw_people):
    people = input()
    if people in no_one_hear_and_saw_people.keys():
        count += 1
        no_one.append(people)

print(count)
no_one.sort()
for i in range(len(no_one)):
    print(no_one[i])