# Задание 3.
#
# Узнайте у пользователя целое положительное число n.
# Найдите сумму чисел n + nn + nnn.
#
# Пример:
# Введите число n: 3
# n + nn + nnn = 369

num_1 = input("Введите целое положительное число n:  ")
num_2 = num_1 + num_1
num_3 = num_1 * 3

print(f"n + nn + nnn =", int(num_1) + int(num_2) + int(num_3))