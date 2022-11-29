# Реализуем числовой ряд Фибоначчи в интервале от 0 до 1000
list = [0, 1] # Инициируем числовой ряд с двумя производными
print(list[len(list) - 2])
print(list[len(list) - 1])
i = 0
while i <= 18: # Ограничим числовой ряд 18-ю итерациями цикла (всего в ряде будет 20 значений)
    i += 1
    prelasttindex = list[len(list) - 2] # Вычисляем индекс предпоследнего значения текущего числового ряда
    lastindex = list[len(list) - 1] # Вычисляем индекс последнего значения текущего числового ряда
    list.append(lastindex + prelasttindex) # Добавляем к ранее инициируемому числовому ряду сумму двух последних чисел в текущем числовом ряду

print(list)












# def fibonacci(index):
#     if index <= 0:
#         return 0
#     elif index == 1:
#         return 1
#     else:
#         result = fibonacci(index - 1) + fibonacci(index - 2)
#     return result

# print(fibonacci(3))

# a = 5
# b = a - 1
# c = a - 2


# print(round(b / (a), 2))
# print(round(c / (a), 2))
