# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

n = int(input("Введите,СКОЛЬКО ВСЕГО У Вас монет: "))
coins = input("Введите расположение монеток, где H - решка, а Т - орел: ")

heads = coins.count("H")  # количество монеток, лежащих вверх решкой
tails = coins.count("T")  # количество монеток, лежащих вверх гербом

min_flips = min(heads, tails)  # выбираем наименьшее из двух чисел

print("Минимальное количество монет, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной, равно:", min_flips)