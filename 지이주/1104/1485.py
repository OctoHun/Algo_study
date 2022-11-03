# 1485 정사각형
import sys

def leng(a,b):
    return (a**2+b**2)**0.5

T = int(input())

for tc in range(T):
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(4)]

    data.sort()
    length = []
    for i in range(3):
        for j in range(i+1,4):
            ans1 = (data[i][0]-data[j][0])**2
            ans2 = (data[i][1]-data[j][1])**2
            length.append(abs(ans1+ans2))
    length.sort()
    if length[0]==length[1] and length[0]==length[2] and length[0]==length[3] and length[4]==length[5]:
        print(1)
    else:
        print(0)
