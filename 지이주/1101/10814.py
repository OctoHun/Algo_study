#10814 나이순정렬 
N = int(input())
data = []
for i in range(N):
    a , b = input().split()
    a = int(a)
    data.append((a,b))
data.sort(lambda x:x[0])
for i in data:
    print(*i)
