money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
total_capital=money_capital+salary
count=0
while total_capital>=spend:
    total_capital-=spend
    count += 1
    total_capital+=salary
    spend+=spend*increase
print("Количество месяцев, которое можно протянуть без долгов:", count)
