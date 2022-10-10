# 가장 큰 수 를 찾아서 그 값을 기준으로
# 에라토스테네스의 체 사용

number_of_prime = int(input())
primes = list(map(int, input().split()))
max_num = max(primes)
che = [1] * (max_num + 1)
# 1은 소수가 아님
che[1] = -1
half_max_num = max_num // 2
for i in range(2, max_num + 1):
    for j in range(i, half_max_num + 1):
        prime = i * j
        if prime > max_num:
            break
        che[prime] = -1

count = 0
for prime in primes:
    if che[prime] == 1:
        count += 1

print(count)