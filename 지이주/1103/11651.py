# 11651 좌표정렬하기 2
import sys
N = int(input())

data = []
for i in range(N):
    a,b = map(int,sys.stdin.readline().split())
    data.append((a,b))
data.sort(lambda x:x[0])
data.sort(lambda x:x[1])
for i in data:
    print(*i)
