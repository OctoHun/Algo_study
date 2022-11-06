pad_size = int(input())
pad = [list(map(int, input().split())) for _ in range(pad_size)]

count_zero = 0
count_plus = 0
count_minus = 0

def check_fill(startX, startY, pad_size):
    global count_minus, count_plus, count_zero
    start_color = pad[startX][startY]
    width = pad_size // 3
    if width == 0:
        if start_color == 1:
            count_plus += 1
        elif start_color == 0:
            count_zero += 1
        else:
            count_minus += 1
        return
    for i in range(startX, startX + pad_size):
        for j in range(startY, startY + pad_size):
            if pad[i][j] != start_color:
                for power1 in range(3):
                    for power2 in range(3):
                        check_fill(startX + (width * power1), startY + (width * power2), pad_size // 3)
                return
    if start_color == 1:
        count_plus += 1
    elif start_color == 0:
        count_zero += 1
    else:
        count_minus += 1

check_fill(0, 0, pad_size)
print(count_minus)
print(count_zero)
print(count_plus)
