number = int(input('enter a three-digit number: '))
digit_1 = number // 100
digit_2 = (number // 10) % 10
digit_3 = number % 10
sum_digits = digit_1 + digit_2 + digit_3
product_digits = digit_1 * digit_2 * digit_3
print(f'sum of digits: {sum_digits}\nproduct_digits: {product_digits}')

#enter a three-digit number: 222
# sum of digits: 6
# product_digits: 8

# enter a three-digit number: 666
# sum of digits: 18
# product_digits: 216