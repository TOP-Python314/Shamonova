def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Введите количество разрядов: "))
count = 0

for number in range(10**(n-1), 10**n):
    if is_prime(number):
        count += 1

print(count)

# Введите количество разрядов: 5
# 8363