#1735 분수합
a,b = map(int,input().split())
c,d = map(int,input().split())

e = a*d+b*c
f = b*d

A , B = max(e,f) , min(e,f)

while A%B!=0:
    ans = A%B
    A = B
    B = ans

if B==1:
    print(f'{e} {f}')
else:
    print(f'{e//B} {f//B}')
