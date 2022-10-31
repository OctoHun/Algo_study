number_of_id, number_of_target = map(int, input().split())

ids = {}
for _ in range(number_of_id):
    id, pw = input().split()
    ids[id] = pw

for _ in range(number_of_target):
    print(ids[input()])