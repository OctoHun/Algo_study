import heapq
import sys
input = sys.stdin.readline

number_of_numbers = int(input())
numbers = []
for _ in range(number_of_numbers):
    number = int(input())
    if number == 0:
        if numbers:
            print(heapq.heappop(numbers))
        else:
            print(0)
    else:
        heapq.heappush(numbers, number)