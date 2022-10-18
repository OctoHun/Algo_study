

T = int(input())

for tc in range(T):
    n = int(input())
    wear = []
    wear_cnt = {}
    for _ in range(n):
        a,b = input().split()
        if b not in wear:
            wear.append(b)
        if b in wear_cnt:
            wear_cnt[b]+=1
        else:
            wear_cnt[b]=1

    ans = 1
    for i in range(len(wear_cnt)):
        ans = ans*(wear_cnt[wear[i]]+1)
    print(ans-1)
