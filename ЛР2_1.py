money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
rezultat_mesyacev = 0
# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов

for mesyats in range(1, 1000):
    itogo_deneg = money_capital + salary

    if itogo_deneg >= spend:
        rezultat_mesyacev = mesyats
        money_capital = itogo_deneg - spend
        rost_cen = spend * increase
        spend = spend + rost_cen
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", rezultat_mesyacev)
