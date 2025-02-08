"""
Помилки (номери рядків через пробіл, цей рядок - №2): 11 14 15
"""


def unemployment_rate(unemployed, employed):
    """Повернути рівень безробіття (РБ) як частку від 1.

       Розрахунок за формулою: РБ = безробітні / (зайняті + безробітні).
    """
    if (unemployed >= 0) and (employed >= 0) and (unemployed + employed != 0):
        return unemployed / (unemployed + employed)
    else:
        raise ValueError("Перевирте початкови дани")

try:
    unemployed = int(input("Введіть кількість безробітних (людей): "))
    employed = int(input("Введіть кількість зайнятих (людей): "))
    rate = unemployment_rate(unemployed, employed)
    print(f"Рівень безробіття = {rate:.1%}")
except ValueError as exc:
    print("Помилка:", exc)
except Exception as exc:
    print("Невидома помилка:", exc)


"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""


def unemployment_rate(unemployed, employed):
    """Повернути рівень безробіття (РБ) як частку від 1.

       Розрахунок за формулою: РБ = безробітні / (зайняті + безробітні).
    """
    return unemployed / (unemployed + employed)


unemployed = int(input("Введіть кількість безробітних (людей): "))
employed = int(input("Введіть кількість зайнятих (людей): "))
rate = unemployment_rate(unemployed, employed)
print(f"Рівень безробіття = {rate:.1%}")
