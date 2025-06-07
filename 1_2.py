
#1
print("Завдання 1")
deg = float(input("градуси по цельсію: "))

print(f"Градуси по Фаренгейту: {deg * 9/5 + 32}F°")

#2
print("Завдання 2")
euro = int(input("Сума в євро: "))
print(f"Ця сума в доларах: {euro * 1.129}") 

#3
print("Завдання 3")
ab = int(input("Ширина: "))
bc = int(input("Висота: "))

print(f"Площа = {ab} * {bc} = {ab*bc} см^2")

#4
print("Завдання 4")
a = int(input("Сторона квадрата: "))
print(F"Периметр квадрата = 4 * {a} = {4*a} см^2")

#5
print("Завдання 5")
number = input("Введіть трицифрове число: ")

a = int(number[0])
b = int(number[1])
c = int(number[2])

suma = a + b + c

print(a)
print(b)
print(c)
print(suma)

#6
print("Завдання 6")
dep = float(input("Введіть суму вкладу: "))
rate = float(input("Введіть річну відсоткову ставку (наприклад, 10 для 10%): "))


for i in range(1, 6):
    dep += dep * (rate / 100)
    print(f"Сума вкладу після {i} року: {round(dep, 2)}")

