tickets_sum = 0
tickets_amount = int(input("Введите количество билетов: "))
for age in range(tickets_amount):
    age = int(input("Введите возраст участника: "))
    if age < 18:
        tickets_sum += 0
    elif 18 <= age < 25:
        tickets_sum += 990
    elif age >= 25:
        tickets_sum += 1390

if tickets_amount > 3:
    discount = int(tickets_sum / 100 * 10)
    print("Стоимость ваших билетов ", tickets_sum - discount)
else:
    print("Стоимость ваших билетов: ", tickets_sum)
