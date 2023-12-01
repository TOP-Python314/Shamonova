number = int(input('enter a three-digit number: '))
digit_1 = number // 100
digit_2 = (number // 10) % 10
digit_3 = number % 10
# УДАЛИТЬ: эти переменные используются каждая только единожды — в их создании нет необходимости
sum_digits = digit_1 + digit_2 + digit_3
product_digits = digit_1 * digit_2 * digit_3
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (язык)
print(f'sum of digits: {sum_digits}\nproduct_digits: {product_digits}')
# КОММЕНТАРИЙ: в случае если вы будете генерировать строку не для человека, а для другой функции/класса/программы — это может стоить вам неработающего приложения


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# enter a three-digit number: 222
# sum of digits: 6
# product_digits: 8

# enter a three-digit number: 666
# sum of digits: 18
# product_digits: 216


# ИТОГ: нужно лучше, доработать — 2/4
