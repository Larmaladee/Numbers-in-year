numberone = float(input("Введите первое число: "))
checknumberone = numberone
numbertwo = float(input("Введите второе число: "))
count = float(input("Введите количество операций: "))
i = 1
while i <= count:
    operation = input("Введите операцию: +,-,/,*,^")
    if operation == "+":
        numberone = numberone + numbertwo
        print(numberone)
        i +=1
    elif operation == "-":
        numberone = numberone-numbertwo
        print(numberone)
        i +=1
    elif operation == "/":
        if numbertwo != 0:
            numberone = numberone/numbertwo
            print(numberone)
            i +=1
        else:
            print("Деление на ноль невозможно")
    elif operation == "*":
        numberone = numberone*numbertwo
        print(numberone)
        i +=1
    elif operation == "^":
        numberone = numberone^numbertwo
        print(numberone)
        i +=1
    else:
        print("Введена неверная операция")
    if i<=count and numberone != checknumberone:
        numbertwo = int(input("Введите второе число: "))
    elif i<=count and numberone != checknumberone:
        numberone = float(input("Введите первое число: "))
        numbetwo = float(input("Введите второе число: "))

