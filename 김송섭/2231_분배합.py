# 1. 주어진 수 N에 대해서 특정 값 X + 각 자리수

N = input()
len_N = len(N)
N = int(N)
for num in range(1, N):
    total = 0
    for i in str(num):
        total += int(i)
    if (num + total) == N:
        print(num)
        break
else:
    print(0)