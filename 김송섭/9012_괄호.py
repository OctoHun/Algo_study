number_of_testcase = int(input())
for _ in range(number_of_testcase):
    stack = []
    parenthesis = input()
    for pa in parenthesis:
        if pa == "(":
            stack.append(pa)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                break
    else:
        if stack:
            print("NO")
        else:
            print("YES")