# 1. 단어가 결과 배열에 있는지 확인하고 없으면 words에 넣어준다.
# 2. 기본 sort로 words를 정렬해준다.
# 3. sort의 key에 단어를 인자로 받으면 길이를 반환하는 함수를 선언하여 한번 더 정렬해준다.

def calc_len(word):
    return len(word)

number_of_words = int(input())
words = []
for i in range(number_of_words):
    word = input()
    # 1
    if word not in words:
        words.append(word)
# 2
words.sort()
# 3
words.sort(key=calc_len)
for word in words:
    print(word)