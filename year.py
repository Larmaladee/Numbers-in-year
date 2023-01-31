year = int(input("Введите год: "))

if(year%4 == 0):
   i = 366
   result = 0
   while (i > 0):
        hundred = 0
        tens = 0
        ones = 0
        if(i>=100):
            chislo = i
            i = i - 1
            hundred = chislo/100
            chislo = chislo % 100
            tens = chislo / 10
            chislo = chislo % 10
            ones = chislo
            result = result + hundred + tens + ones
        elif (i>=10):
            chislo = i
            i = i - 1
            tens = chislo / 10
            chislo = chislo % 10
            ones = chislo
            result = result + tens + ones
        else:
            chislo = i
            i = i - 1
            result = result + chislo
else:
    i = 365
    result = 0
    while (i > 0):
        hundred = 0
        tens = 0
        ones = 0
        if(i>=100):
            chislo = i
            i = i - 1
            hundred = chislo/100
            chislo = chislo % 100
            tens = chislo / 10
            chislo = chislo % 10
            ones = chislo
            result = result + hundred + tens + ones
        elif (i>=10):
            chislo = i
            i = i - 1
            tens = chislo / 10
            chislo = chislo % 10
            ones = chislo
            result = result + tens + ones
        else:
            chislo = i
            i = i - 1
            result = result + chislo
print(int(result))