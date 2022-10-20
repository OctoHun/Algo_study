import sys

def push_front(num):
    deq.insert(0, num)

def push_back(num):
    deq.append(num)

def pop_front():
    if deq:
        print(deq.pop(0))
    else:
        print(-1)

def pop_back():
    if deq:
        print(deq.pop())
    else:
        print(-1)

def size():
    print(len(deq))

def empty():
    if deq:
        print(0)
    else:
        print(1)

def front():
    if deq:
        print(deq[0])
    else:
        print(-1)

def back():
    if deq:
        print(deq[len(deq) - 1])
    else:
        print(-1)

number_of_command = int(input())
deq = []
for _ in range(number_of_command):
    # command = input().split()
    command = sys.stdin.readline().split()
    if len(command) == 2:
        locals()[command[0]](int(command[1]))
    else:
        locals()[command[0]]()