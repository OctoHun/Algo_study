# - 기호부터 +가 나오는 만큼까지 괄호 치기

expression = input().split("-")
result = sum(map(int, expression[0].split("+")))
for index in range(1, len(expression)):
    result -= sum(map(int, expression[index].split("+")))

print(result)