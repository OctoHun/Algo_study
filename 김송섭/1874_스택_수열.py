n = int(input())

# 1. 수를 차례대로 받으며 i(1부터 n까지 차례대로)와 비교
# 2. 받은 숫자 포함까지 i를 push
# 3. current_num까지 받으면 당연히 해당하는 pop은 일치
# 4. 하지만 그 이후에 바로 pop할수있는 수(stack[-1])와 같은 input이 아니라면 False

stack = []
result = []
is_right = True
i = 1
for _ in range(n):
    # 1
    current_num = int(input())
    # 2
    while i <= current_num:
        stack.append(i)
        result.append("+")
        i += 1
    # 3
    if stack[-1] == current_num:
        stack.pop()
        result.append("-")
    # 4
    else:
        is_right = False
        break

if is_right:
    for calc in result:
        print(calc)
else:
    print("NO")