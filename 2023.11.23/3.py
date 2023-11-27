year = float(input('enter a year: '))
if year%4==0 and year%100>0:
    print(f'the {year} is a leap year')
elif year%400==0:
    print(f'the {year} is a leap year')
else:
    print(f'the {year} is not a leap year')
    
# D:\For course\Scripts\Shamonova\2023.11.23>3.py
# enter a year: 400
# the 400.0 is a leap year

# D:\For course\Scripts\Shamonova\2023.11.23>3.py
# enter a year: 404
# the 404.0 is a leap year

# D:\For course\Scripts\Shamonova\2023.11.23>3.py
# enter a year: 2023
# the 2023.0 is not a leap year