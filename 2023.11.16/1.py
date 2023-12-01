name = input('enter your name: ')
surname = input('enter your surname: ')
year_of_birth = int(input('enter your year of birth: '))
age = 2023 - year_of_birth
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (лишний пробел)
print(surname, name, ',', age)
# КОММЕНТАРИЙ: в случае если вы будете генерировать строку не для человека, а для другой функции/класса/программы — это может стоить вам неработающего приложения


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# enter your name: mariia
# enter your surname: shamonova
# enter your year of birth: 1995
# КОММЕНТАРИЙ: должно быть shamonova mariia, 28
# shamonova mariia , 28


# ИТОГ: хорошо, но можно лучше — 2/3


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/
