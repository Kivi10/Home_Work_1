# Найдите сумму цифр трехзначного числа.

a = int(input("Введите число -> "))
sum = int (0)

while a > 0:
    b = int(a % 10)
    sum = sum + b
    a = a / 10

print("Сумма цифр в числе =", sum)