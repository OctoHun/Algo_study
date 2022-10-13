import sys
input = sys.stdin.readline

number_of_command = int(input())
stack = []
stack_len = 0

for _ in range(number_of_command):
    command_input = input().split()
    command = command_input[0]
    if command == "push":
        stack.append(int(command_input[1]))
        stack_len += 1
    elif command == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
            stack_len -= 1
    elif command == "size":
        print(stack_len)
    elif command == "empty":
        if stack:
            print(0)
        else:
            print(1)
    else:
        if not stack:
            print(-1)
        else:
            print(stack[stack_len - 1])