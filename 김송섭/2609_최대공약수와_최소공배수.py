# 1. 두 수의 약수를 구한다
# 2. 겹치는 수들의 곱 = 최대공약수
# 3. 안 겹치는 수를 다른 한 수에 곱한 값 = 최소공배수

def find_factor(num):
    factor = []
    i = 2
    while num != 1:
        if num % i == 0:
            factor.append(i)
            num = num // i
        else:
            i += 1
    return factor

num1, num2 = map(int, input().split())

num1_factor = find_factor(num1)
num2_factor = find_factor(num2)

common_factor = []
for i in range(len(num1_factor)):
    for j in range(len(num2_factor)):
        if num1_factor[i] == num2_factor[j]:
            common_factor.append(num1_factor[i])
            num2_factor[j] = -1
            break
result1 = 1
result2 = 1

for factor in common_factor:
    result1 *= factor
print(result1)

for factor in num2_factor:
    if factor != -1:
        result2 *= factor

print(result2 * num1)