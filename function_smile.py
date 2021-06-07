"""Функция, которая принимает символы ( ) : в любых сочетаниях и возвращать итоговый счет по количеству веселых
и грустных смайликов, которые составляются из переданной последовательности символов.

Примеры:
1.happiness_number(":):(") ➞ -1
2.happiness_number("(:)") ➞ 2
3.happiness_number("::::") ➞ 0

Примечания:
  • веселые смайлики :) и (: оцениваются в 1 балл,
  • грустные смайлики :( и ): оцениваются в -1 балл."""

"""Из символов ( ) : можно составлять веселые и грустные смайлики. Для целей этой задачи:

веселые смайлики :) и (: оцениваются в 1 балл,
грустные смайлики :( и ): оцениваются в -1 балл.
Напишите функцию, которая будет принимать символы ( ) : в любых сочетаниях и возвращать итоговый счет по 
количеству веселых и грустных смайликов, которые составляются из переданной последовательности символов.

Рабочий пример
 happiness_number(":):(") ➞ -1
 # Первые два символа составляют :)        +1      Итого: 1
 # Второй и третий символы составляют ):     -1      Итого: 0
 # Третий и четвертый символы составляют :(      -1      Итого: -1
Другие примеры
 happiness_number(":):(") ➞ -1
 happiness_number("(:)") ➞ 2
 happiness_number("::::") ➞ 0"""


# Варианты решений

def happiness_number(s):
    return s.count(':)') + s.count('(:') - s.count(':(') - s.count('):')


def happiness_number(s):
    c = 0
    for a, b in zip(s, s[1:]):
        if a + b in (':)', '(:'): c += 1
        if a + b in (':(', '):'): c -= 1
    return c
