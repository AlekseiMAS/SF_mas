# 1. Напишите программу, которой на вход подается последовательность чисел через пробел, а также запрашивается у пользователя любое число.

# 2. В качестве задания повышенного уровня сложности можете выполнить проверку соответствия указанному в условии ввода данных.
# Далее программа работает по следующему алгоритму:
# 2.1 Преобразование введённой последовательности в список
# 2.2 Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)
# 2.3 Устанавливается номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу.
# При установке позиции элемента воспользуйтесь алгоритмом двоичного поиска, который был рассмотрен в этом модуле. Реализуйте его также отдельной функцией.
###########################################################################

error = 'Ошибка ввода данных, перезапустите программу!'
sequence_numbers = input('Введите целые числа через пробел: ')
user_number = int(input('Введите любое число: '))
###########################################################################

# Функция для определения цифр в строке

def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False
###########################################################################

# Проверка соответствия условию ввода данных

if " " not in sequence_numbers:
    print("\nВы забыли поставить пробел между числами (см. условие)")
    sequence_numbers = input('Введите целые числа через пробел: ')
if not is_int(sequence_numbers):
    print('\nВы указали не целые числа, либо другие символы (введите целые числа, см. условие)\n')
    print(error)
else:
    sequence_numbers = sequence_numbers.split()

# 2.1 Замена списка строк на список чисел

list_sequence_numbers = [int(item) for item in sequence_numbers]
###########################################################################

# 2.2 Сортировка списка

def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

###########################################################################
list_sequence_numbers = merge_sort(list_sequence_numbers)
###########################################################################

# 2.3 Установка позиции элемента

def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'
###########################################################################

# Устанавливается номер позиции элемента, который меньше
# введенного пользователем числа, а следующий за ним больше или равен этому числу.

print(f'Упорядоченный по возрастанию список: {list_sequence_numbers}')

if not binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers)):
    rI = min(list_sequence_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_sequence_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {list_sequence_numbers[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_sequence_numbers.index(rI)}
В списке нет меньшего элемента''')
    elif rI > user_number:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {list_sequence_numbers.index(rI)}
Ближайший меньший элемент: {list_sequence_numbers[min_ind]} его индекс: {min_ind}''')
    elif list_sequence_numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_sequence_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(list_sequence_numbers, user_number, 0, len(list_sequence_numbers))}')