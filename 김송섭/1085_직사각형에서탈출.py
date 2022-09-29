x, y, w, h = map(int, input().split())
# 현재 위치에서 상하좌우 크기를 배열에 저장
distance = [x, y, abs(x - w), abs(y - h)]
# 그중에 가장 작은 값을 출력
print(min(distance))
