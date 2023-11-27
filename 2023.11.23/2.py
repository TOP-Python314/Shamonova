number1 = float(input('enter first integer: '))
number2 = float(input('enter second integer: '))

if number1%number2>0:
    print(f"""{number1} cannot be divided by {number2} without a remainder
    quotient {number1//number2}
	remainder {number1%number2}""")
else:
    print(f"""{number1} can be divided by {number2} without a remainder
    quotient {number1//number2}""")
    
# D:\For course\Scripts\Shamonova\2023.11.23>2.py
# enter first integer: 5
# enter second integer: 6
# 5.0 cannot be divided by 6.0 without a remainder
    # quotient 0.0
        # remainder 5.0

# D:\For course\Scripts\Shamonova\2023.11.23>2.py
# enter first integer: 6
# enter second integer: 3
# 6.0 can be divided by 3.0 without a remainder
    # quotient 2.0