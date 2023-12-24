def fibonacci_sequence(n):
    sequence = [1, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence

n = int(input("Введите количество чисел последовательности Фибоначчи: "))
result = fibonacci_sequence(n)
print(result)

# Введите количество чисел последовательности Фибоначчи: 22
# [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711]