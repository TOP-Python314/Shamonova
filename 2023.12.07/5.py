word = input("Введите слово: ")
scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}
points = 0
for letter in word:
    for i in scores_letters:
        if letter.upper() in scores_letters[i]:
            points += i
            break
        
print(points)

# Введите слово: морковка
# 11

# Введите слово: синхрофазотрон
# 29