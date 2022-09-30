N = int(input())

data = []
for i in range(N):
    data.append(input())
ans = [[] for _ in range(N+1)]

for i in range(N):
    for j in range(1,51):
        if len(data[i]) == j:
            ans[j].append(data[i])
            break

for i in range(N+1):
    if ans[i]:
        ans[i].sort()
result = []
for i in range(N+1):
    if ans[i]:
        for j in ans[i]:
            if j not in result:
                result.append(j)
for i in range(len(result)):
    print(result[i])