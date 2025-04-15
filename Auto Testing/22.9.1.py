<<<<<<< HEAD
same_list = list(map(int, input("Введите последовательность чисел: ").split()))
if len(same_list) != 0:
    print("Верно!")
any_num = int(input("Введите любое число: "))
if type(any_num) == int:
    print("Верно!")

for i in range(len(same_list)):
    idx_min = i
    for j in range(i, len(same_list)):
        if same_list[j] < same_list[idx_min]:
            idx_min = j
    if i != idx_min:
        same_list[i], same_list[idx_min] = same_list[idx_min], same_list[i]


def binary_search(same_list, any_num, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if same_list[middle] == any_num:
        return middle
    elif any_num < same_list[middle]:

        return binary_search(same_list, any_num, left, middle - 1)
    else:
        return binary_search(same_list, any_num, middle + 1, right)

print(same_list)

left = int(same_list[0])
right = int(same_list[-1])
if any_num < left and any_num > right:
    print("Числа нет в диапазоне.")
else:
    print(binary_search(same_list, any_num, 0, len(same_list) - 1))
=======
same_list = list(map(int, input("Введите последовательность чисел: ").split()))
if len(same_list) != 0:
    print("Верно!")
any_num = int(input("Введите любое число: "))
if type(any_num) == int:
    print("Верно!")

for i in range(len(same_list)):
    idx_min = i
    for j in range(i, len(same_list)):
        if same_list[j] < same_list[idx_min]:
            idx_min = j
    if i != idx_min:
        same_list[i], same_list[idx_min] = same_list[idx_min], same_list[i]


def binary_search(same_list, any_num, left, right):
    if left > right:
        return False

    middle = (right + left) // 2
    if same_list[middle] == any_num:
        return middle
    elif any_num < same_list[middle]:

        return binary_search(same_list, any_num, left, middle - 1)
    else:
        return binary_search(same_list, any_num, middle + 1, right)

print(same_list)

left = int(same_list[0])
right = int(same_list[-1])
if any_num < left and any_num > right:
    print("Числа нет в диапазоне.")
else:
    print(binary_search(same_list, any_num, 0, len(same_list) - 1))
>>>>>>> 1c8d10041864e99f0db21dc83707bcddd0d90cd8
