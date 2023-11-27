first = input('enter the coordinates of the first square of the chessboard: ')
second = input('enter the coordinates of the second square of the chessboard: ')
if first[0] == second[0] and first[1] == second[1]:    
    print('no')
elif first[0] == second[0] or first[1] == second[1]:
    print('yes')
else:
    print('no')

# D:\For course\Scripts\Shamonova\2023.11.23>5.py
# enter the coordinates of the first square of the chessboard: b1
# enter the coordinates of the second square of the chessboard: b1
# нет

# D:\For course\Scripts\Shamonova\2023.11.23>5.py
# enter the coordinates of the first square of the chessboard: b2
# enter the coordinates of the second square of the chessboard: v2
# да

# D:\For course\Scripts\Shamonova\2023.11.23>5.py
# enter the coordinates of the first square of the chessboard: a1
# enter the coordinates of the second square of the chessboard: a5
# да