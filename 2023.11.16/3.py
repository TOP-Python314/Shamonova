minutes = int(input('введите минуты: '))
# ИСПОЛЬЗОВАТЬ везде: PEP 8 не рекомендует отделять скобки вызова от имени функции
# ИСПРАВИТЬ: вывод не соответствует требуемому формату (язык)
print(f'{minutes} минут = {minutes // 60} часов {minutes % 60} минут')
# КОММЕНТАРИЙ: в случае если вы будете генерировать строку не для человека, а для другой функции/класса/программы — это может стоить вам неработающего приложения

# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# number of minutes: 500
# 500 minutes = 8 hours 20 minutes

# ИТОГ: хорошо, доработать — 2/3

# после изменений кода
# введите минуты: 70
# 70 минут = 1 часов 10 минут