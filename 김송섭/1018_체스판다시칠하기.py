# 1. 체스판을 pad에 입력받음
# 2. slice를 통해 pad를 8*8이 되도록 자르며 반복
# 3. 시작점을 두 가지로 나누어 criteria에 대입
# 4. criteria를 기준으로 짝수와 홀수로 나누어 변경되는 색의 수만큼 count
# 5. 그 count가 최소인지 비교

def find_change_count(pad, criteria):
    count = 0
    for i in range(8):
        for j in range(8):
            if j % 2 == 0 and i % 2 == 0:
                if pad[j][i] != criteria:
                    count += 1
            elif j % 2 == 1 and i % 2 == 1:
                if pad[j][i] != criteria:
                    count += 1
            else:
                if pad[j][i] == criteria:
                    count += 1
    return count

M, N = map(int, input().split())
# 1
pad = [list(input()) for _ in range(M)]
min_count = 50 * 50
# 2
for i in range(M - 8 + 1):
    for j in range(N - 8 + 1):
        new_pad = [pad[i + k][j:j+8] for k in range(8)]
        # 3, 4
        count1 = find_change_count(new_pad, "B")
        count2 = find_change_count(new_pad, "W")
        # 5
        count = min([count1, count2])
        if count < min_count:
            min_count = count

print(min_count)