pad_size = int(input())

pad = [list(map(int, input())) for _ in range(pad_size)]
result = ""
def compress_pad(startX, startY, pad_size):
    global result
    criteria_num = pad[startX][startY]
    for i in range(startX, startX + pad_size):
        for j in range(startY, startY + pad_size):
            if pad[i][j] != criteria_num:
                result += "("
                compress_pad(startX, startY, pad_size // 2)
                compress_pad(startX, startY + pad_size // 2, pad_size // 2)
                compress_pad(startX + pad_size // 2, startY, pad_size // 2)
                compress_pad(startX + pad_size // 2, startY + pad_size // 2, pad_size // 2)
                result += ")"
                return
    if criteria_num == 1:
        result += "1"
    else:
        result += "0"

compress_pad(0, 0, pad_size)
print(result)
