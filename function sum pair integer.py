"""Функция будет принимать любое число. Из цифр этого числа нужно будет составить пары и сложить получившиеся числа.
Функция должна вернуть сумму чисел, составленных из пар цифр.
Для составления пары берем первую и последнюю цифру числа, продвигаясь от краев к центру."""

# Пример с разбором
# closing_in_sum(2520) ➞ 72
# Первая и последняя цифры - 2 и 0.
# Из цифр 2 и 0 составляем число 20.
# Вторая и предпоследняя цифра - 5 и 2.
# Из цифр 5 и 2 составляем число 52.
# 20 + 52 = 72


# Другие примеры
# closing_in_sum(121) ➞ 13
# 11 + 2
# closing_in_sum(1039) ➞ 22
# 19 + 3
# closing_in_sum(22225555) ➞ 100
# 25 + 25 + 25 + 25


"""Примечания
Если передано число с нечетным количеством цифр, центральную цифру просто прибавляем к общей сумме (см. пример 1).
Нуль тоже считаем отдельной цифрой (см. пример 2)."""


# Варианты решений
def closing_in_sum(n):
    n = str(n)
    if len(n) <= 2:
        return int(n)
    return int(n[0] + n[-1]) + closing_in_sum(n[1:-1])


from itertools import zip_longest


def closing_in_sum(n):
    s = str(n)
    half = len(s) // 2
    return sum(
        int(i + j)
        for i, j in zip_longest(s[:half], s[half:], fillvalue='0')
    )


def zipper(a, b):
    return sum([int(x + y) for x, y in zip(a, b)])


def closing_in_sum(num):
    n = str(num)
    l = len(n)
    a = n[:l // 2]
    b = n[l // 2 + 1:] if l % 2 else n[l // 2:]
    c = n[l // 2]
    return zipper(a, b) + int(c) if l % 2 else zipper(a, b)
