number1 = float(input('enter first number: '))
number2 = float(input('enter second number: '))
number3 = float(input('enter third number: '))
if number1<0 and number2<0 and number3<0:
    print('no positive numbers')
elif number1>0 and number2<0 and number3<0:
    print(f'sum of positive numbers{number1}')
elif number1<0 and number2>0 and number3<0:
    print(f'sum of positive numbers{number2}')
elif number1<0 and number2<0 and number3>0:
    print(f'sum of positive numbers{number3}')
elif number1<0 and number2>0 and number3>0:
    print(f'sum of positive numbers{number2+number3}')  
elif number1>0 and number2<0 and number3>0:
    print(f'sum of positive numbers{number1+number3}')
elif number1>0 and number2>0 and number3<0:
    print(f'sum of positive numbers{number1+number2}')
else:
    print(f'sum of positive numbers{number1+number2+number3}')
    
# D:\For course\Scripts\Shamonova\2023.11.23>1.py
# enter first number: 1
# enter second number: 1
# enter third number: 1
# sum of positive numbers3.0

# D:\For course\Scripts\Shamonova\2023.11.23>1.py
# enter first number: -1
# enter second number: -1
# enter third number: -1
# no positive numbers

# D:\For course\Scripts\Shamonova\2023.11.23>1.py
# enter first number: -1
# enter second number: 1
# enter third number: 1
# sum of positive numbers2.0

# D:\For course\Scripts\Shamonova\2023.11.23>1.py
# enter first number: 1
# enter second number: -1
# enter third number: 1
# sum of positive numbers2.0