K , N = map(int,input().split())

data = list(int(input()) for _ in range(K))
s = 1
e = max(data)
while s<=e: # 이분법 구현!!!
    mid = (s+e)//2 
    cnt = 0
    for i in range(len(data)):
        cnt += data[i]//mid
    if cnt>=N:
        s = mid+1
    else:
        e= mid-1
print(e)
