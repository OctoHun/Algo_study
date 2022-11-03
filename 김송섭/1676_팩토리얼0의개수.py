number = int(input())

pac = 1
for power in range(2, number + 1):
    pac *= power

pac = str(pac)
if len(pac) == 1:
    if pac == '0':
        print(1)
    else:
        print(0)
else:
    count = 0
    for i in range(len(pac) - 1, 0, -1):
        if pac[i] != '0':
            print(count)
            break
        else:
            count += 1