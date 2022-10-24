number_of_cards = int(input())
cards = list(map(int, input().split()))
number_of_needs = int(input())
needs = list(map(int, input().split()))

cards_dict = {}
for card in cards:
    if card in cards_dict.keys():
        cards_dict[card] += 1
    else:
        cards_dict[card] = 1

for need in needs:
    if need in cards_dict.keys():
        print(cards_dict[need], end=" ")
    else:
        print(0, end=" ")