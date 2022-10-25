amount_of_sugar = int(input())

max_5kg = amount_of_sugar // 5
for number_of_5kg in range(max_5kg, -1, -1):
    calced_sugar = amount_of_sugar - (number_of_5kg * 5)
    if calced_sugar % 3 == 0:
        print(number_of_5kg + (calced_sugar // 3))
        break
else:
    print(-1)