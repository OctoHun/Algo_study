# 산술평균: 값을 입력 받을 때마다 다 더해주기
# 중앙값: 그냥 배열 다 받아서 정렬 해야할듯?
# 최빈값: 나오는 수들을 딕셔너리로 저장하여 value로 count
# 범위: 최소 최대값을 따로 저장

number_of_input = int(input())
# 중앙값을 위해
numbers = []
# 산술평균을 위해
sum = 0
# 범위를 위해
max_num = -4001
min_num = 4001
# 최빈값을 위해
num_dict = {}
for _ in range(number_of_input):
    number = int(input())
    sum += number
    if number > max_num:
        max_num = number
    if number < min_num:
        min_num = number
    numbers.append(number)
    if number not in num_dict.keys():
        num_dict[number] = 1
    else:
        num_dict[number] += 1

numbers.sort()
print(round(sum / number_of_input))
print(numbers[number_of_input // 2])
max_count = 0
same_counts = []
for key in num_dict.keys():
    if num_dict[key] > max_count:
        max_count = num_dict[key]
        same_counts = [key]
    elif num_dict[key] == max_count:
        same_counts.append(key)
if len(same_counts) == 1:
    print(same_counts[0])
else:
    same_counts.sort()
    print(same_counts[1])
print(max_num - min_num)