salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен



# TODO Оформить решение
def homeless(salary, spend, months, increase):
    need_money = 0  # количество денег, чтобы прожить 10 месяцев
    for i in range(months):
        need_money = need_money - salary + spend * (1 + increase)**i
    return round(need_money)
print(homeless(salary, spend, months, increase))

