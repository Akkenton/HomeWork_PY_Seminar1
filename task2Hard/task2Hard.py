# Задача 2: - HARD необязательная, идет за 3 обязательных.  
# Найдите сумму цифр любого вещественного или целого числа. Можно использовать decimal. Через строку решать нельзя.

#Комментарий: Обработчик ошибко не пишем, считаем, что пользователь правильно вводит вещественное число



from decimal import Decimal                 #Используем Decimal
count = Decimal(input('Введите число: '))
intPart = count//1                          #Записываем отдельно дробную и целую части в переменные floatPart и intPart соответственно
floatPart = count % 1
print('Дробная часть: ', floatPart)
print('Целая часть: ', intPart)

while type(floatPart) == Decimal:           #цикл для перевода дробной части в целое число
    if (floatPart % 1) == 0:
        floatPart = int(floatPart)
    else:
        floatPart = floatPart*10

summ = 0                                    #Объявляем переменную суммы

while floatPart > 0:                        #Цикл для подсчета суммы чисел бывшей дробной части
    summ = floatPart % 10+summ
    floatPart = round(floatPart/10)

while intPart > 0:                          #Цикл для подсчета суммы чисел целой части
    summ = intPart % 10 + summ
    intPart = round(intPart/10)

print('Сумма чисел заданого1 числа: ', summ)