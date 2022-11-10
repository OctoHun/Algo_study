# 11725 트리의 부모찾기
import sys
#오랜만이라 bfs도 제대로 구현 못하겠다.
# 더 좋은 풀이법이 있을것 같지만 일단 해결했으니 도망쳐!!
def bfs():
    q = []
    for i in data[1]:
        q.append(i)
        ans[i]=1
    while q:
        a = q.pop(0)
        if visit[a]==0:
            visit[a]=1
            for j in data[a]:
                if visit[j]==0:
                    q.append(j)
                    ans[j]=a

N = int(input())
data = [[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    data[a].append(b)
    data[b].append(a)
ans = [0]*(N+1)
visit=[0]*(N+1)
bfs()
for i in range(2,N+1):
    print(ans[i])
