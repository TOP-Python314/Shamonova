mile_1 = input('enter first part of a mile: ')
mile_2 = input('enter second part of a mile: ')
miles_result = float(mile_1 + '.' + mile_2)
kilometers_result = miles_result * 1.61
# ИСПОЛЬЗОВАТЬ везде: PEP 8 не рекомендует отделять скобки вызова от имени функции
print(f'{miles_result} miles = {kilometers_result:.2f} kilometers')


# enter first part of a mile: 1
# enter second part of a mile: 2
# 1.2 miles = 1.93 kilometers

# enter first part of a mile: 55
# enter second part of a mile: 77
# 55.77 miles = 89.79 kilometers

