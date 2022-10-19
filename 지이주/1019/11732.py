# 11732 집합

# list와 set 간의 연산속도 차이가 꽤나난다는걸 알 수 있는 문제다.
# 처음에는 리스트로 풀어보려 했으나 계속해서 시간초과 , 메모리에러가 발생했다.
# 그래서 구글링결과 이문제에서 list는 시간복잡도가 O(N)인 반면 set은 O(1)이라더라.
# 그래서 적용시켜보니 바로 통과가 나왔다.
import sys
M = int(sys.stdin.readline())
S = set()
for _ in range(M):
    data = sys.stdin.readline().split()

    if len(data)==1:
        if data[0] == 'all':
            S = set([i for i in range(1,21)])
        elif data[0] == 'empty':
            S = set()
    else:
        data[1] = int(data[1])
        if data[0] == 'add':
            S.add(data[1])
        elif data[0] == 'remove':
            if data[1] in S:
                S.discard(data[1])
        elif data[0] == 'check':
            if data[1] in S:
                print(1)
            else:
                print(0)
        elif data[0] == 'toggle':
            if data[1] in S:
                S.discard(data[1])
            else:
                S.add(data[1])

