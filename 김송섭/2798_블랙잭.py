
result = []
def combination(len_original, N):
    if N == 0:
        result.append(combi[:])
        # print(combi)
    elif len_original < N:
        return
    else:
        combi[N - 1] = cards[len_original - 1]
        combination(len_original - 1, N - 1)
        combination(len_original - 1, N)

number_of_cards, shouting_number = map(int, input().split())
cards = list(map(int, input().split()))

combi = [-1] * 3
len_original = len(cards)
combination(len_original, 3)
max_num = 0
for numbers in result:
    total = sum(numbers)
    if total > max_num and total <= shouting_number:
        max_num = total
print(max_num)