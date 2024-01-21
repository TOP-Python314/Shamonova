def checking(list1, list2):
    if not list2:
        return True
    if not list1:
        return False
    for i in range(len(list1)):
        if list1[i] == list2[0]:
            if list1[i:i+len(list2)] == list2:
                return True
    return False

input1 = input()
input2 = input()

list1 = list(map(int, input1.split()))
list2 = list(map(int, input2.split()))

if checking(list1, list2):
    print("да")
else:
    print("нет")

# 1 1 2 2 3
# 2 2
# да

# 567890
# 89
# нет


# 4
# нет