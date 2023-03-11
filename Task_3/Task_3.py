# Программа которая проверяет является ли номер на билете счастливым.

tiketNumber = int(input("Введите шестизначный номер билета -> "))
tn = tiketNumber
sumRight = int(0)
sumLeft = int(0)
count = int(0)
while tn > 0:
    tn = int(tn / 10)
    count += 1
if count != 6:
    print("Количество цифр не соответсвует условию.")
else:
    while count > 0:
        if count > 3:
            sumRight = sumRight + (tiketNumber % 10)
            tiketNumber = int(tiketNumber/10)
            count -= 1
        else:
            sumLeft = sumLeft + (tiketNumber % 10)
            tiketNumber = int(tiketNumber/10)
            count -= 1
    if sumLeft == sumRight:
        print("Поздравляю, у вас счастливый билетик, приятного аппетита :)")
    else:
        print("К сожалению билетик не счастливый, в следующий раз повезет :)")
