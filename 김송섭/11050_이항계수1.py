def nCk(N, K):
    total1 = 1
    total2 = 1
    for _ in range(K):
        total1 *= N
        N -= 1
    for _ in range(K, 1, -1):
        total2 *= K
        K -= 1

    return total1 // total2

numbers = list(map(int, input().split()))
print(nCk(numbers[0], numbers[1]))