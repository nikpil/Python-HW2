number = int(input("Введите неомер месяца: "))
if number <= 12 and number >= 1:
    month_dict = {1: 'Зима',
                  2: 'Зима',
                  3: 'Весна',
                  4: 'Весна',
                  5: 'Весна',
                  6: 'Лето',
                  7: 'Лето',
                  8: 'Лето',
                  9: 'Осень',
                  10: 'Осень',
                  11: 'Осень',
                  12: 'Зима'}
    month_list = list(month_dict.values())
    for i, el in enumerate(month_list):
        if i == number-1:
            print(f"Решение через 'list'. Это {month_list[i]}")
            print(f"Решение через 'dict'. Это {month_dict[number]}")



