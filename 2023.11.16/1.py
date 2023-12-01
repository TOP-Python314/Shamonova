name = input('enter your name: ')
surname = input('enter your surname: ')
year_of_birth = int(input('enter your year of birth: '))
age = 2023 - year_of_birth
print(surname, name, ',', age)


# ИСПОЛЬЗОВАТЬ везде: PEP 8 рекомендует добавлять пробелы после символа # — в большинстве редакторов кода, включая Notepad++, это делает команда "Вкл./Выкл. комментарий"
# enter your name: mariia
# enter your surname: shamonova
# enter your year of birth: 1995
# shamonova mariia , 28


# КОММЕНТАРИЙ: PEP 8 — сборник рекомендаций по стилистическому оформлению Python кода — их стоит использовать для большего удобства чтения своего и чужого кода: https://peps.python.org/pep-0008/
