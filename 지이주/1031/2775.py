# 2775

T = int(input())



for tc in range(T):
    # k층 n호
    k = int(input())
    n = int(input())
    data = [[0]*(n+1) for _ in range(15)]
    for i in range(15):
        data[i][0] = 1
    data[14][1] = 2
    for i in range(13,-1,-1):
        data[i][1] = data[i+1][0] + data[i+1][1]


    for i in range(2,n):
        data[14][i] = i+1
        for j in range(13,-1,-1):
            data[j][i] = data[j+1][i]+data[j][i-1]


    print(data[14-k][n-1])
