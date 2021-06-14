"""Функция, принимающую в виде аргументов два списка и определяющую, являются ли они противоположными друг другу.
Функция должна возвращать True или False."""

# Каждая пара списков будет состоять из одинаковых элементов (типа a и b). Список считается анти-списком,
# если все элементы в нем противоположны соответствующим элементам в первом списке.

"""Примеры
is_anti_list(["1", "0", "0", "1"], ["0", "1", "1", "0"]) ➞ True

is_anti_list(["apples", "bananas", "bananas"], ["bananas", "apples", "apples"]) ➞ True

is_anti_list([3.14, True, 3.14], [3.14, False, 3.14]) ➞ False"""


# Примечание
# Исходим из того, что в каждой паре списков будут элементы только двух видов.

# 1 вариант

def is_anti_list(lst1, lst2):
    return all({a, b} == set(lst1) for a, b in zip(lst1, lst2))


# 2 вариант

def is_anti_list(lst1, lst2):
    seen = set()
    for i, j in zip(lst1, lst2):
        seen.update((i, j))
        if i == j or len(seen) > 2:
            return False
    return True
