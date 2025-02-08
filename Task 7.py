"""
Помилки (номери рядків через пробіл, цей рядок - №2): 11 14 15
"""


def power(x, y=2):
    """Повернути x^y."""
    if y == 0:
        return 1
    elif y < 0:
        raise ValueError(f"у значення не може бути вид'емним ({y})")
    else:
        return x * power(x, y - 1)

try:
    x = int(input("x="))
    y = int(input("y="))
    print(power(x, y))
except ValueError as exc:
    print("Введите целое число", exc)


"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def power(x, y=2):
    """Повернути x^y."""
    if y == 0:
        return 1
    else:
        return x * power(x, y - 1)


x = int(input("x="))
y = int(input("y="))
print(power(x, y))
