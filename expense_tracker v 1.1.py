income = float(input("Введите ежемесячный доход: "))

while True:
    if income < 0:
        print('Доход не может быть отрицательным.')
        income = float(input('Введите ежемесячный доход: '))
    else:
        break

expense_count = int(input('Введите количество расходов: '))
total_expenses = 0

while True:
    if expense_count <= 0:
        print('Кол-во расходов не может быть равно нулю или меньше нуля.')
        expense_count = int(input('Введите количество расходов повторно: '))
    else:
        break

for i in range(expense_count):
    print('Расход №', i + 1)
    while True:
        expense = (float(input('Введите расход: ')))
        if expense < 0:
            print('Отрицательный расход не допустим.')
        else:
            break
    total_expenses += expense

remainder = round(income - total_expenses, 2)

if income > 0:
    spent_percent = (total_expenses / income) * 100
print()

print('===== ФИНАНСОВЫЙ ОТЧЕТ =====')
print()

print('Доход:', round(income, 2))
print('расходы:', round(total_expenses, 2))
print('Остаток:', round(remainder, 2))
if income > 0:
    print('Потрачено:', round(spent_percent, 2), '%')
else:
    print('Процент расходов рассчитать невозможно')
if remainder > 0:
    print('Уложились в бюджет!')
elif remainder == 0:
    print('Потратили весь доход.')
else:
    print('Превысили бюджет(')

print()

print('============================')
