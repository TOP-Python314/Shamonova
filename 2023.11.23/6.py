first = input('enter the coordinates of the first square of the chessboard: ')
second = input('enter the coordinates of the second square of the chessboard: ')
if first[0] == second[0] and first[1] == second[1]:    
    print('no')
elif ord(first[0]) - 1 <= ord(second[0]) <= ord(first[0]) + 1 and int(first[1]) - 1 <= int(second[1]) <= int(first[1]) + 1:
    print('yes')
else:
    print('no')

# D:\For course\Scripts\Shamonova\2023.11.23>6.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: a1
# no

# D:\For course\Scripts\Shamonova\2023.11.23>6.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: a2
# yes

# D:\For course\Scripts\Shamonova\2023.11.23>6.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: a3
# no

# D:\For course\Scripts\Shamonova\2023.11.23>6.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: b1
# yes

# D:\For course\Scripts\Shamonova\2023.11.23>6.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: b2
# yes

# D:\For course\Scripts\Shamonova\2023.11.23>6.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: c2
# no