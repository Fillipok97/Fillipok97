<<<<<<< HEAD
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму"))
deposit = [
    int(per_cent['ТКБ'] * money / 100),
    int(per_cent['СКБ'] * money / 100),
    int(per_cent['ВТБ'] * money / 100),
    int(per_cent['СБЕР'] * money / 100)]
print(deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))
=======
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму"))
deposit = [
    int(per_cent['ТКБ'] * money / 100),
    int(per_cent['СКБ'] * money / 100),
    int(per_cent['ВТБ'] * money / 100),
    int(per_cent['СБЕР'] * money / 100)]
print(deposit)
print("Максимальная сумма, которую вы можете заработать -", max(deposit))
>>>>>>> 1c8d10041864e99f0db21dc83707bcddd0d90cd8
