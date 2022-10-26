import sys
number_of_numbers = int(input())

numbers = [0] * 10001
for _ in range(number_of_numbers):
    numbers[int(sys.stdin.readline())] += 1

for i in range(1, 10001):
    if numbers[i] != 0:
        for _ in range(numbers[i]):
            print(i)