while True:
    numbers = list(map(int, input().split()))
    if sum(numbers) == 0:
        break
    max_num = 0
    max_index = -1
    zero = 0
    num_arr = []
    for num in numbers:
        if num > max_num:
            num_arr.append(max_num)
            max_num = num
        else:
            num_arr.append(num)

    if max_num ** 2 == (num_arr[1] ** 2) + (num_arr[2] ** 2):
        print("right")
    else:
        print("wrong")