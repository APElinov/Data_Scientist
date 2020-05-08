number_of_avocados = int(input("Сколько авакадо вы хотите купить? "))

cost_r, cost_k = map(int, input("Укажите стоимость руб. "
                                "и коп. через пробел: ").split())

summ_cost = cost_r * 100 + cost_k
summ_r = summ_cost * number_of_avocados // 100
summ_k = summ_cost * number_of_avocados % 100

print('Итого:', summ_r, 'руб.', summ_k, 'коп.')
