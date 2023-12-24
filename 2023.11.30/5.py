massage = input('Введите сообщение: ')
count = len(massage.replace(" ", ""))
amount = count * 30	
print(f'{amount//100} руб. {amount%100} коп.')

# Введите сообщение: мама мыла раму
# 3 руб. 60 коп.