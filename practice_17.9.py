"""Напишите программу, которой на вход подается
последовательность чисел через пробел,
а также запрашивается у пользователя любое число.
Далее программа работает по следующему алгоритму:

Преобразование введённой последовательности в список

Сортировка списка по возрастанию элементов в нем (для реализации сортировки определите функцию)

Устанавливается номер позиции элемента, который меньше введенного пользователем
 числа, а следующий за ним больше или равен этому числу."""

import random

def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


# array = list(random.randint(0, 100) for i in range(0, random.randint(10, 15)))   # генератор списка натуральных чисел
# print("Список случайно сгенерированных чисел : ", array)

array = list(map(int, input("Введите числа через пробел : ").split()))

def bubble_sort():     # сорторивка пузырьком
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    print("Отсортированный спиок :", array)
bubble_sort()

element = int(input("Введите число : "))

try:
    x = binary_search(array, element, 0, len(array))
    if x is False:
        print("Числа", element, "меньше любого числа из списка ")

    else:
        print("Число", element,"есть в списке с индексом", x, "\n", "Индекс ближайщего элемента, который меньше =", x - 1,
        "\n", "Индекс ближайщего элемента, который больше =", x + 1)

except IndexError as e:
    print("Число", element, "больше любого числа из списка")




