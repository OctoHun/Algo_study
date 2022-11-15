n, m = map(int, input().split())
s = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    s.append(list(input()))
# 현재위치 저장
queue = [[0, 0]]
s[0][0] = 1
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        # 1인 칸으로 이동, 역류 금지
        if 0 <= x < n and 0 <= y < m and s[x][y] == "1":
            queue.append([x, y])
            # 이동한 현재 위치에 1씩 추가
            s[x][y] = s[a][b] + 1
print(s[n - 1][m - 1])