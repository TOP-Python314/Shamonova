email = input("Введите имейл: ")

if "@" in email and "." in email:
    print("да")
else:
    print("нет")
    
# Введите имейл: mariia@gmail.com
# да

# Введите имейл: mariia@ru
# нет