while True:
    sentence = input()
    if sentence == ".":
        break
    qu_stack = []
    is_right = True
    for a in sentence:
        if a == "[" or a == "(":
            qu_stack.append(a)
        elif a == "]":
            if not qu_stack or qu_stack.pop() != "[":
                is_right = False
                break
        elif a == ")":
            if not qu_stack or qu_stack.pop() != "(":
                is_right = False
                break

    if qu_stack or not is_right:
        print("no")
    else:
        print("yes")