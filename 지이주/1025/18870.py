#18870 μ’νμμΆ

import sys

N = int(input())
data = list(map(int,sys.stdin.readline().split()))

ans = sorted(set(data))
# print(ans)
dic = {ans[i]: i for i in range(len(ans))}
# print(dic)
for i in data:
    print(dic[i],end=' ')
