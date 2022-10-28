def comb():
    for i in range(1<<N):
        res = []
        for j in range(N):
            if i & (1<<j):
                res.append(data[j])
        if len(res)==M:
            ans.append(res)

N , M = map(int,input().split())
data = [0]*N
for i in range(N):
    data[i] = i+1

ans = []
comb()
ans = sorted(ans)
for i in range(len(ans)):
    print(*ans[i])
