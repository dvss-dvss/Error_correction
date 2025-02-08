"""
Помилки (номери рядків через пробіл, цей рядок - №2): 9 15 16
"""


# Наведено список ПІБ. Знайдіть найпоширеніше по-батькові.
# Якщо немає по-батькові, людина не враховується в розрахунку.

try:
    n = int(input("Введіть кількість людей: "))


    middle_names = {}
    for i in range(n):
        fio = input("Введіть ПІБ через пробіл: ").split()
        try:
            middle_name = fio[2]
            middle_names[middle_name] = middle_names.get(middle_name, 0) + 1
        except IndexError:
            pass

    print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
    print("Людей брало участь у розрахунку:", n)
except ValueError as exc:
    print("Помилка:", exc, "Перевиртте початкови дани")
except IndexError as exc:
    print("Помилка:", exc, "Перевиртте початкови дани")
except Exception as exc:
    print("Помилка:", exc)


"""
Помилки (номери рядків через пробіл, цей рядок - №2):
"""


# Наведено список ПІБ. Знайдіть найпоширеніше по-батькові.
# Якщо немає по-батькові, людина не враховується в розрахунку.

n = int(input("Введіть кількість людей: "))

middle_names = {}
for i in range(n):
    fio = input("Введіть ПІБ через пробіл: ").split()

    middle_name = fio[2]
    middle_names[middle_name] = middle_names.get(middle_name, 0) + 1

print(sorted(middle_names.items(), key=lambda item: item[1])[-1][0])
print("Людей брало участь у розрахунку:", n)
