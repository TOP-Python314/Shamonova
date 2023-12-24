numbers = []

while True:
    number = int(input('введите число: '))
    if number % 7 == 0:
        numbers.append(number)
    else:
        print(' '.join(map(str, reversed(numbers))))
        break

# введите число: 7
# введите число: 14
# введите число: 21
# введите число: 28
# введите число: 5
# 28 21 14 7