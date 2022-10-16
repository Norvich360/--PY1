money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05



# TODO Оформить решение
def homeless(money_capital, salary,spend,increase):
    month = 0  # количество месяцев, которое можно прожить
    while money_capital > spend * (1+increase)**month:
        money_capital = money_capital + salary - spend * (1 + increase)**month
        month += 1
    return month
print(homeless(money_capital, salary,spend,increase))

