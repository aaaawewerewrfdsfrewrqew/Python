a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

print("Сума:", a + b + c)
print("Добуток:", a * b * c)

d1 = float(input("Введіть довжину першої діагоналі: "))
d2 = float(input("Введіть довжину другої діагоналі: "))

area = (d1 * d2) / 2
print("Площа ромба:", area)

zp = float(input("Зарплата за місяць: "))
credit = float(input("Платіж за кредит: "))
utilities = float(input("Комунальні послуги: "))

leftover = zp - credit - utilities
print("Залишилось після всіх виплат:", leftover)

distance = float(input("Відстань в км: "))
fuel_usage = float(input("Витрата пального (л/100км): "))
cl = float(input("Ціна за літр бензину: "))

cost = (distance / 100) * fuel_usage * cl
print("Вартість поїздки:", cost)

total = float(input("Загальна сума рахунку: "))
people = int(input("Кількість осіб: "))

tip = total * 0.15
total_with_tip = total + tip
per_person = total_with_tip / people

print("Чайові: {:.2f}".format(tip))
print("Сума з чайовими: {:.2f}".format(total_with_tip))
print("Кожен має заплатити: {:.2f}".format(per_person))

daily_price = float(input("Ціна оренди за день: "))
days = int(input("Кількість днів оренди: "))
deposit = float(input("Сума застави: "))

total_cost = (daily_price * days) + deposit
without_deposit = daily_price * days

print("Загальна вартість (з заставою):", total_cost)
print("Вартість оренди без застави:", without_deposit)