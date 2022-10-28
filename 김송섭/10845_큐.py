from sys import stdin

q = []
count = 0
len_q = 0
def push(X):
    global len_q
    q.append(X)
    len_q += 1

def pop():
    global count
    global len_q
    if len_q:
        print(q[count])
        count += 1
        len_q -= 1
    else:
        print(-1)

def size():
    global len_q
    global count
    print(len_q)

def empty():
    global count
    global len_q
    if len_q:
        print(0)
    else:
        print(1)

def front():
    global count
    global len_q
    if len_q:
        print(q[count])
    else:
        print(-1)

def back():
    global count
    global len_q
    if len_q:
        print(q[len(q) - 1])
    else:
        print(-1)

number_of_cammands = int(stdin.readline())
for _ in range(number_of_cammands):
    command = stdin.readline().split()
    if command[0] == "push":
        push(command[1])
    else:
        locals()[command[0]]()