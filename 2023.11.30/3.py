number = int(input("Введите число: "))
total_sum = 0

for i in range(1, number+1):
    if number % i == 0:
        total_sum += i

print(total_sum)

# Введите число: 56
# 120