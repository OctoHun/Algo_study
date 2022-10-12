# 마지막에 도달하면 그날 밤은 안 미끄러짐
# 그냥 하루 양으로 나누면 마지막에 미끄러지는 것이 포함됨
# 미끄러지는 하루를 전체에서 빼주면 마지막에 미끄러지는 걸 감안해줄 수 있음
# 하루동안 올라가는 양으로 나누었을 때 나머지가 있으면 하루 더 가야함
day_climb, night_slip, tree_height = map(int, input().split())

day = (tree_height - night_slip) // (day_climb - night_slip)
rest = (tree_height - night_slip) % (day_climb - night_slip)
if rest == 0:
    print(day)
else:
    print(day + 1)