"""
Напишіть функцію визначення кількості днів у конкретному місяці.
Ваша функція повинна приймати два параметри: month - номер місяця у вигляді цілого числа в діапазоні від 1 до 12 і year - рік,
що складається із чотирьох цифр. Перевірте, чи функція коректно обробляє місяць лютий високосного року.
"""

from datetime import date


def get_days_in_month(month, year):
    if month == 12:
        month_end = 1
        year_end = year + 1
    else:
        month_end = month + 1
        year_end = year
    
    d1 = date(year=year, month=month, day=1)
    d2 = date(year=year_end, month=month_end, day=1)

    return (d2 - d1).days


print(get_days_in_month(2, 2024))
