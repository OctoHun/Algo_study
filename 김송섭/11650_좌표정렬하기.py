# 마찬가지로 입력을 받는 수가 많으면 입력 받는데 시간이 많이 걸려서
# input = sys.stdin.readline 를 사용해야함

def point_sort(point):
    return (point[0], point[1])

number_of_point = int(input())
points = [list(map(int, input().split())) for _ in range(number_of_point)]

points.sort(point_sort)

for point in points:
    print(point[0], point[1])