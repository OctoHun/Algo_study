number_of_computers = int(input())
number_of_pairs = int(input())
pair_dict = {}
warmed = []
for _ in range(number_of_pairs):
    start_com, end_com = map(int, input().split())
    if start_com not in pair_dict.keys():
        pair_dict[start_com] = [end_com]
    else:
        pair_dict[start_com].append(end_com)
    if end_com not in pair_dict.keys():
        pair_dict[end_com] = [start_com]
    else:
        pair_dict[end_com].append(start_com)

def find_warm(start_com):
    for com in pair_dict[start_com]:
        if com not in warmed:
            warmed.append(com)
            find_warm(com)

find_warm(1)
if 1 in warmed:
    print(len(warmed) - 1)
else:
    print(len(warmed))