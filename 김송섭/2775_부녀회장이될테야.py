number_of_testcase = int(input())
for test in range(number_of_testcase):
    # floor는 0층부터 시작이라 floor = k
    # address는 b호까지, 1호부터 시작이라 address = b - 1
    floor_number = int(input())
    address = int(input())
    apartment = [[first_floor for first_floor in range(1, address + 1)]]
    # 2차원 배열로 0층부터 append
    # 직전 배열의 1호 ~ b호의 합으로 새로운 배열
    for fl in range(1, floor_number + 1):
        floor = []
        for ad in range(1, address + 1):
            total = 0
            for h in range(ad):
                total += apartment[fl - 1][h]
            floor.append(total)
        apartment.append(floor)
    print(apartment[floor_number][address - 1])