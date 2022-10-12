number_of_point = int(input())
points = [list(map(int, input().split())) for _ in range(number_of_point)]

def point_sort(point):
    return (point[1], point[0])

points.sort(key=point_sort)

for point in points:
    print(point[0], point[1])