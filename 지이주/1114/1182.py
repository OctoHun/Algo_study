# 1182 부분수열의 합
import sys

def comb():
    global ans
    for i in range(1<<N):
        res = []
        for j in range(N):
            if i & (1<<j):
                res.append(data[j])
        if res and sum(res)==S:
            ans+=1

N , S = map(int,input().split())
data = list(map(int,sys.stdin.readline().split()))

ans = 0
comb()
print(ans)
