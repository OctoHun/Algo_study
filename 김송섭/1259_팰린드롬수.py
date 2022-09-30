# 1. input으로 0이 들어올때까지 반복
# 2. 들어온 값 num의 처음과 끝의 인덱스 i, j로 안쪽으로 들어오면서 비교
# 3. num // 2 길이만큼 성공하면 팰린드롬 수

# 1
while True:
    num = int(input())
    str_num = str(num)
    if num == 0:
        break
    # 2
    i, j = 0, len(str_num) - 1
    # 3
    for _ in range(len(str_num) // 2):
        if str_num[i] != str_num[j]:
            print("no")
            break
        i += 1
        j -= 1
    else:
        print("yes")