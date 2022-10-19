number_of_bill = int(input())

numbers = []
for _ in range(number_of_bill):
    number = int(input())
    if number == 0:
        numbers.pop()
    else:
        numbers.append(number)


print(sum(numbers))