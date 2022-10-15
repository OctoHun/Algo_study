number_of_member = int(input())

def member_sort(members):
    return (members[0], members[2])

members = []
for i in range(number_of_member):
    input_member = input().split()
    members.append([int(input_member[0]), input_member[1], i])

members.sort(key=member_sort)
for member in members:
    print(member[0], member[1])