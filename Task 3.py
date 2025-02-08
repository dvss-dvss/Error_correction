"""
Помилки (номери рядків через пробіл, цей рядок - №2): 23 24
"""


def first_vacant_row(seats):
    """Повернути перший ряд, в якому є найбільше
    вільних місць та їх кількість.

    Повертається нумерація рядів із 1. Якщо вільних місць немає, повернути 0, 0.

    Параметры:
        - seats (list of list): інформація про продані квитки
                                (1 - продано, 0 - ні).

    Результат:
        - tuple (ряд, кількість місць).
    """
    max_count = 0
    max_row = 0
    for row_index, row in enumerate(seats):
        available_seats_count = row.count(0)  # 0 - пусто
        if available_seats_count > max_count:
            max_row = row_index + 1
            max_count = available_seats_count

    return max_row, max_count

from random import randint
from pprint import pprint

seats = [[randint(0,1)for _ in range(10)] for _ in range (10)]
pprint(seats)
pprint(first_vacant_row(seats))

"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def first_vacant_row(seats):
    """Повернути перший ряд, в якому є найбільше
    вільних місць та їх кількість.

    Повертається нумерація рядів із 1. Якщо вільних місць немає, повернути 0, 0.

    Параметры:
        - seats (list of list): інформація про продані квитки
                                (1 - продано, 0 - ні).

    Результат:
        - tuple (ряд, кількість місць).
    """
    max_count = 0
    max_row = 0
    for row_index, row in enumerate(seats):
        available_seats_count = row.count(0)  # 0 - пусто
        if available_seats_count >= max_count:
            max_row = row_index
            max_count = available_seats_count

    return max_row, max_count
