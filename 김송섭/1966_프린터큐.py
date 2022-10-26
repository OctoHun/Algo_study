# 그냥 큐로 뒤에 자신보다 큰게 있으면 뒤로 넘기기
number_of_testcase = int(input())

for _ in range(number_of_testcase):
    number_of_paper, paper_location = map(int, input().split())
    importance_list = list(map(int, input().split()))
    result = 0
    while True:
        if importance_list[0] == max(importance_list):
            if paper_location == 0:
                result += 1
                print(result)
                break
            else:
                importance_list.pop(0)
                paper_location -= 1
                result += 1
        else:
            importance_list.append(importance_list.pop(0))
            if paper_location == 0:
                paper_location = len(importance_list) - 1
            else:
                paper_location -= 1
