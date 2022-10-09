room_number = int(input())

n = 1
num = 1
while num < room_number:
    num += 6 * n
    n += 1
print(n)
