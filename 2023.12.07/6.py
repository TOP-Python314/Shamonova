def is_binary_number(s):
    if s.startswith('0b'):
        s = s[2:]
    elif s.startswith('b'):
        s = s[1:]
    
    for char in s:
        if char != '0' and char != '1':
            return False
    return True

number = input("введите двоичное число: ")
if is_binary_number(number):
    print("да")
else:
    print("нет")
    
# введите двоичное число: 101010
# да

# введите двоичное число: 0b1010
# да

# введите двоичное число: 1b101010
# нет