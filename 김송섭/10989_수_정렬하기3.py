# 입력 데이터의 개수가 많을 때는 sys.stdin.readline()을
# 사용해야한다는...

number_of_num = int(input())
numbers = [0] * 10001

for i in range(number_of_num):
    num = int(input())
    numbers[num] += 1

for i in range(10001):
    num = numbers[i]
    if num:
        for _ in range(num):
            print(i)