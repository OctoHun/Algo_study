# 4963 섬의개수
import sys
sys.setrecursionlimit(10**6)
def dfs(i,j):
    global cnt
    # for i in range(h):
    #     for j in range(w):
    if data[i][j] == 1:
        for k in range(8):
            ni = i + di[k]
            nj = j + dj[k]
            while 0<=ni<h and 0<=nj<w and visit[ni][nj]==0 and data[ni][nj] == 1:
                visit[ni][nj] = 1
                dfs(ni,nj)


while True:
    w , h = map(int,input().split())
    if w==0 and h == 0:
        break
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    visit = [[0]*w for _ in range(h)]
    cnt = 0
    di = [-1,1,0,0,-1,1,1,-1]
    dj = [0,0,-1,1,1,1,-1,-1]
    island = []
    for i in range(h):
        for j in range(w):
            if data[i][j]==1:
                island.append((i,j))
    for i,j in island:
        if visit[i][j]==0:
            dfs(i,j)
            cnt+=1
    print(cnt)
