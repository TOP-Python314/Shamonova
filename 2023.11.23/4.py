first = input('enter the coordinates of the first square of the chessboard: ')
second = input('enter the coordinates of the second square of the chessboard: ')
coordinates1 = ord(first[0]) + int(first[1])
coordinates2 = ord(second[0]) + int(second[1])
if coordinates1 % 2 == 0 and coordinates2 % 2 == 0:
    print('yes')
elif coordinates1 % 2 != 0 and coordinates2 % 2 != 0:
    print('yes')    
else: 
	print('no')
    
# D:\For course\Scripts\Shamonova\2023.11.23>4.py
# enter the coordinates of the first square of the chessboard: b1
# enter the coordinates of the second square of the chessboard: b3
# yes

# D:\For course\Scripts\Shamonova\2023.11.23>4.py
# enter the coordinates of the first square of the chessboard: f4
# enter the coordinates of the second square of the chessboard: f5
# no