def search_in_dict(input_dict, value):
    for key, val in input_dict.items():
        if val == value:
            return key
    return "! value error !"

input_dict = {}
while True:
    input_str = input("Введите число и строку: ")
    if not input_str:
        break
    num, string = input_str.split()
    input_dict[int(num)] = string

search_value = input("Введите значение для поиска: ")

result = search_in_dict(input_dict, search_value)
print(result)

# Введите число и строку: 1 мама
# Введите число и строку: 2 папа
# Введите число и строку: 3 сестра
# Введите число и строку: 4 брат
# Введите число и строку:
# Введите значение для поиска: брат
# 4

# Введите число и строку: 1 яблоко
# Введите число и строку: 2 банан
# Введите число и строку: 3 апельсин
# Введите число и строку: 5 груша
# Введите число и строку: 6 киви
# Введите число и строку:
# Введите значение для поиска: банан
# 2

# Введите число и строку: 1 a
# Введите число и строку: 2 b
# Введите число и строку: 3 c
# Введите число и строку:
# Введите значение для поиска: r
# ! value error !