def calculate_months(money_capital, salary, spend, increase):
    months = 0

    while money_capital >= 0:
        money_capital += salary
        money_capital -= spend

        months += 1

        spend *= (1 + increase)

    return months


money_capital = 100000  # Финансовая подушка безопасности
salary = 50000  # Ежемесячная зарплата
spend = 40000  # Расходы на проживание
increase = 0.05  # Рост цен

months_without_debts = calculate_months(money_capital, salary, spend, increase)
print(months_without_debts)