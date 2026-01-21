salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
nado_protyanut = 0

for month in range (1, months + 1):
    deficit = spend - salary
    nado_protyanut = nado_protyanut + deficit
    rost_cen = spend * increase
    spend = spend + rost_cen
itogo = round(nado_protyanut)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", itogo)
