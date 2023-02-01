import array as arr 

class Calculate:
    def count(index,i):
        result = 0
        while (i >= 0):
            tens = 0
            ones = 0
            if (i>=10):
                chislo = i
                i = i - 1
                tens = int( chislo / 10)
                chislo = int(chislo % 10)
                ones = chislo
                result =int( result + tens + ones)
            else:
                chislo = i
                i = i - 1
                result = result + chislo
        return result

year = int(input("Введите год: "))


if(year%4 == 0):
   days = arr.array("i",[31,29,31,30,31,30,31,31,30,31,30,31])
   itog = 0
   i = 0
   method = Calculate()
   while (i<12):
    arrayargument = days[i]
    itog = itog + method.count(arrayargument)
    i = i +1
else:
    days = arr.array("i",[31,28,31,30,31,30,31,31,30,31,30,31])
    itog = 0
    i = 0
    method = Calculate()
    while (i<12):
        arrayargument = days[i]
        itog = itog + method.count(arrayargument)
        i = i +1
   
print(int(itog))

