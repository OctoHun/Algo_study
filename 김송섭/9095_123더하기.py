number_of_testcase = int(input())

def is_zero(total):
    global count

    if total == 0:
        count += 1
        return
    elif total < 0:
        return
    else:
        for i in range(1, 4):
            is_zero(total - i)

for _ in range(number_of_testcase):
    total = int(input())
    count = 0
    is_zero(total)
    print(count)