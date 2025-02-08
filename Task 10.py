"""
Помилки (номери рядків через пробіл, цей рядок - №2): 26 34
"""


# Програма містить словник результатів НМТ іспит = бал.
# Дізнайтеся, чи заявник зможе вступити, якщо вам потрібно сдати
# Усі ці іспити не менше мінімальної кількості балів.

min_grades = {
    "Історія": 180,
    "Математика": 185,
    "Українська мова": 175
}

print("""Щоб визначити можливість вступу, необхідна інформація про вас.

Щоб ввести іспит і бали, введіть їх через |: Історія | 140.
Щоб завершити введення, натисніть кнопку Enter.
""")

exams = {}
while True:
    line = input("").strip()
    if line == "":
        break


    try:
        exam, grade = [x.strip() for x in line.split("|")]
        exams[exam] = int(grade)
    except ValueError:
        print("Помилка - повторить дани")

print("Ваші іспити:")
for i, (exam, grade) in enumerate(exams.items(), start=1):
    print(f"{i}) {exam} {grade}")

ok = False
for exam_name, min_grade in min_grades.items():
    try:
        if exams[exam_name] < min_grade:
            break
    except KeyError:
        print(f"Видсутня оцинка за испит {exam}")
        break
else:
    ok = True

print("Ви можете вступити до нас!" if ok else "На жаль...")


"""
Помилки (номери рядків через пробіл, цей рядок - №2): !!!
"""

# Програма містить словник результатів НМТ іспит = бал.
# Дізнайтеся, чи заявник зможе вступити, якщо вам потрібно сдати
# Усі ці іспити не менше мінімальної кількості балів.

min_grades = {"Історія": 180, "Математика": 185, "Українська мова": 175}

print(
    """Щоб визначити можливість вступу, необхідна інформація про вас.

Щоб ввести іспит і бали, введіть їх через |: Історія | 140.
Щоб завершити введення, натисніть кнопку Enter.
"""
)

exams = {}
while True:
    line = input("").strip()
    if line == "":
        break

    exam, grade = [x.strip() for x in line.split("|")]
    exams[exam] = int(grade)

print("Ваші іспити:")
for i, (exam, grade) in enumerate(exams.items(), start=1):
    print(f"{i}) {exam} {grade}")

ok = False
for exam_name, min_grade in min_grades.items():
    if exams[exam_name] < min_grade:
        break
else:
    ok = True

print("Ви можете вступити до нас!" if ok else "На жаль...")
