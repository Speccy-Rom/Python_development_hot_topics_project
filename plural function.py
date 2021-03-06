# Функция, которая будет принимать существительные в единственном числе и возвращать те же существительные,
# но если какие-то из них встречаются больше одного раза, именно эти слова должны возвращаться во множественном числе.

# Примеры

# """pluralize(["cow", "pig", "cow", "cow"]) ➞ { "cows", "pig" }
# pluralize(["table", "table", "table"]) ➞ { "tables" }
# pluralize(["chair", "pencil", "arm"]) ➞ { "chair", "pencil", "arm" }"""

"""Примечания
Передаваться будут только слова на английском языке.
Для упрощения будем считать, что множественное число всегда образуется путем добавления окончания s.
Варианты решений"""


def pluralize(lst):
    return set(i + 's' * (lst.count(i) > 1) for i in lst)


def pluralize(lst):
    return {i + 's' if lst.count(i) > 1 else i for i in lst}
