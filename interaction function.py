"""Функция, которая принимает две строки, состоящие из знаков «+» и «-», и возвращает строку — результат их взаимодействия.
Исходим из того, что строки, передаваемые в функцию, всегда будут равной длины.
Переданные строки взаимодействуют следующим образом:
плюс и плюс дают плюс
минус и минус дают минус
плюс и минус нейтрализуют друг друга и вместе дают 0.

Разбор примера
 neutralise("+-+", "+--") ➞ "+-0"
 # Сравниваем первые символы двух строк, потом следующие два символа и т.д.
 # "+" и "+" возвращают "+".
 # "-" и "-" возвращают "-".
 # "+" и "-" возвращают "0".
 # Возвращаем строку символов. 

Другие примеры
 neutralise("--++--", "++--++") ➞ "000000"
 neutralise("-+-+-+", "-+-+-+") ➞ "-+-+-+"
 neutralise("-++-", "-+-+") ➞ "-+00" """


def neutralise(s1, s2):
    return ''.join(a if a == b else '0' for a, b in zip(s1, s2))


def neutralise(s1, s2):
    return ''.join(s1[i] if s1[i] == s2[i] else '0' for i in range(len(s1)))


neutralise = lambda a, b: "".join(["0", x][x == y] for x, y in zip(a, b))
