# 최소한 하나라도 입으면 됨 == (옷 가지수 + 아예 안 입는 경우(1)) * 옷 종류 만큼 반복 = 모든 경우의 수. 여기에 다 벗는 경우 1 빼기

number_of_testcase = int(input())
for _ in range(number_of_testcase):
    number_of_wear = int(input())
    wear = {}
    for _ in range(number_of_wear):
        wearing, location = input().split()
        if location in wear.keys():
            wear[location] += 1
        else:
            wear[location] = 1
    total = 1
    for value in wear.values():
        total *= (value + 1)

    print(total - 1)